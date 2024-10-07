#!/usr/bin/python
from __future__ import print_function, division
import re
import glob
import datetime as dt
import os
import time
import sys
import socket
import struct
import numpy as np
from collections import deque, defaultdict
from math import cos
import subprocess
from xml.etree import ElementTree
import matplotlib
import pylab as pl
import pyfftw
from argparse import ArgumentParser, RawTextHelpFormatter
import xml.dom.minidom

# Constants
ROOT_Hashirama = '/home/shining/study/MS/vLITE/logs/logs/'
ROOT_Nrl = '/home/vlite-master/mtk/logs/'
ROOT = ROOT_Hashirama
NE = '/tmp/'
PROMFILE = 'one.prom'
NODENAME = 'vlite-difx12'
TIMESLEEP = 5
GLOBEXP = ROOT + '*' + NODENAME + '_writer*.log'
TIMESTAMP_REGEX = r"^(\[\d{4}-\d{2}-\d{2}-\d{1,2}:\d{2}:\d{2}\])"
TIMESTAMP_SIG = "[%Y-%m-%d-%H:%M:%S]"

stime = lambda x: dt.datetime.strptime(x, TIMESTAMP_SIG).strftime('%s')

entry = re.compile(
    TIMESTAMP_REGEX +
    r"(.*\n)"
)

trigger_group = ('224.3.29.71', 20003)
reader_group = ('224.3.29.71', 20000)
writer_group = ('224.3.29.71', 20001)
multicast_group = '239.192.3.2'
server_address = ('', 53001)
HEIMDALL_PORT = 27555
TRIGGER_PORT = 27556
FRAMESPERSEC = 25600


def tailf(fline):
    fline.seek(0, os.SEEK_END)
    while True:
        line = fline.readline()
        if not line:
            time.sleep(TIMESLEEP)
            continue
        yield line


def parser(lines, match):
    log = []
    for xlin in tailf(lines):
        sre = match(xlin)
        if sre:
            yield sre.group(1), log
            log = []
            log.append(sre.group(2).strip())
        else:
            log.append(xlin.strip())
    yield sre.group(1), log


def getter(gEXP):
    fil = max(glob.iglob(gEXP), key=os.path.getctime)
    print(fil)
    fl = open(fil, 'r')
    for ts, x in parser(fl, entry.match):
        if "ObservationDocument:" in x:
            srcname = x[4].split(' = ')[1]
            ret = "#HELP obspar Observation parameters\n"
            ret = ret + "#TYPE obspar gauge\n"
            ret = ret + '{0} obspar {{"sourcename"="{1}";"nodename"="{2}"}} 1\n'.format(stime(ts), srcname, NODENAME)
            ofile.write(ret)
            ofile.flush()
        xfil = max(glob.iglob(gEXP), key=os.path.getctime)
        if xfil == fil:
            continue
        else:
            fl.close()
            fl = open(xfil, 'r')
            fil = xfil


def server_setup(nmax=18):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('vlite-nrl', HEIMDALL_PORT))
    s.listen(nmax)
    return s


def send_trigger(trigger_struct):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.2)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.sendto(trigger_struct, trigger_group)
    sock.close()


def send_char(char, multicast_group):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.2)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.sendto(char, multicast_group)
    sock.close()


def parse_host_configuration(conf_file):
    with open(conf_file, 'r') as f:
        lines = filter(lambda l: len(l) > 0, map(str.strip, f.readlines()))
    return lines


def main():
    parser = ArgumentParser(
        description=(
            "Multi-function script for working with VLITE-fast.\n\n"
            "Usage examples:\n"
            "  python script.py --log            # Parse logs\n"
            "  python script.py --send_trigger   # Send a trigger event\n"
            "  python script.py --config <file>  # Load a configuration file\n"
            "  python script.py --command <cmd>  # Send a custom command to multicast\n"
        ), formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('--log', action='store_true', help='Parse logs')
    parser.add_argument('--send_trigger', action='store_true', help='Send Trigger')
    parser.add_argument('--config', type=str, help='Load configuration file.')
    parser.add_argument('--command', type=str, help='Send custom command to multicast.')

    args = parser.parse_args()

    if args.log:
        with open(NE + PROMFILE, 'w') as ofile:
            getter(GLOBEXP)
    
    if args.send_trigger:
        t0 = time.time() - 1
        t1 = t0 + 1e-6
        msg = "Recorded data segment"
        trigger_struct = struct.pack('dd128s', t0, t1, msg.encode('utf-8'))
        send_trigger(trigger_struct)

    if args.config:
        conf_lines = parse_host_configuration(args.config)
        print("Configuration Loaded: ")
        for line in conf_lines:
            print(line)

    if args.command:
        send_char(args.command.encode('utf-8'), writer_group)
        time.sleep(0.01)
        send_char(args.command.encode('utf-8'), reader_group)


if __name__ == '__main__':
    main()

