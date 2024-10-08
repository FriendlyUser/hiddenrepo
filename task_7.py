import asyncio
import unittest
import json
import uuid
from collections import defaultdict
from datetime import timedelta
import logging
import time
import aiofiles
from aiofiles import os as aio_os

# Constants
DELIMITER = "$"
QUORUM_COUNT = 0.5


# Exceptions
class RaftLogException(Exception):
    pass


# RaftLog Implementation
class RaftLog:
    def __init__(self, file_name):
        self.log = []
        self.file_name = file_name
        self.commit_len = 0

    async def initialize(self):
        await self._load_logs()

    async def _load_logs(self):
        try:
            async with aiofiles.open(self.file_name, 'r+') as f:
                async for line in f:
                    msg, term = line.strip().split(DELIMITER)
                    self.log.append((msg, int(term)))
        except FileNotFoundError:
            pass

    def append(self, data) -> None:
        self.log.append(data)

    async def commit(self):
        if self.commit_len > self.length():
            raise RaftLogException(
                f"entries in the committed files: ${self.commit_len} are greater than the log entries :${self.length()}")

        async with aiofiles.open(self.file_name, 'a') as f:
            for entry in self.log[self.commit_len:]:
                await f.write(entry[0] + DELIMITER + str(entry[1]) + "\n")

        self.commit_len = len(self.log)

    def length(self):
        return len(self.log)

    def get(self, start: int, end: int):
        return self.log[start:end]

    def truncate(self, index: int):
        if index < self.commit_len:
            raise RaftLogException(
                f"provided index: {index} is less than the commit index")
        self.log = self.log[:index - 1]


# NodeServer Implementation
class NodeServer:
    async def __init__(self, host, port, peers=None):
        self.host = host
        self.port = port
        self.peers = set(peers) if peers is not None else set()

        self.raft_index = 0
        self.current_term = 0
        self.last_term = 0
        self.voted_for = None
        self.data_log = RaftLog("default_log")
        await self.data_log.initialize()
        self.leader = None

        self.heartbeat = timedelta(seconds=5)
        self.timeout = 1
        self._clients = [NodeClient(*peer, timeout=self.timeout, node=self)
                         for peer in self.peers]

        self.id = uuid.uuid1()
        self.sent_length = defaultdict(int)
        self.acked_length = defaultdict(int)

    async def broadcast(self, writer, data, ping=False):
        if self.leader != self.id:
            return

        self.data_log.append((data['msg'], data['term']))
        self.acked_length[self.id] = self.data_log.length()

        queue = asyncio.Queue()

        for follower in self._clients:
            await queue.put((follower, self.sent_length[follower.id]))

        consumer = [asyncio.create_task(
            self._consumer(queue)) for _ in range(5)]

        await queue.join()
        [c.cancel() for c in consumer]

        resp = self.commit_logs()
        writer.writelines([bytes(b) for b in resp])
        await writer.drain()

    async def _consumer(self, queue):
        while True:
            follower, prefix_length = await queue.get()


# NodeClient Implementation
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._reader = None
        self._writer = None
        self.open = False

    async def connect(self):
        if not self.open:
            self._reader, self._writer = await asyncio.open_connection(self.host, self.port)
            self.open = True

    async def readline(self):
        await self.connect()
        data = await self._reader.readline()
        return data

    def write(self, data):
        return self._writer.write(data)

    def close(self):
        return self._writer.close()

    async def drain(self):
        await self._writer.drain()

    def disconnect(self):
        if self.open:
            self._writer.close()


class NodeClient:
    def __init__(self, host, port, id, **kwargs):
        self.remote_host = host
        self.remote_port = port
        self.conn = Connection(self.remote_host, self.remote_port)
        self.id = id
        self.timeout = kwargs.get("timeout", None)
        node = kwargs.get("node", None)
        if node:
            self.node_host = node.host
            self.node_port = node.port

    def disconnect(self):
        self.conn.disconnect()


# Testing Suites

class RaftLogTestSuite(unittest.IsolatedAsyncioTestCase):
    def __init__(self, *args, **kwargs):
        super(RaftLogTestSuite, self).__init__(*args, **kwargs)
        self.file_name = "test_log_file"

    async def asyncSetUp(self):  # Use async setUp
        self.logger = RaftLog(self.file_name)
        await self.create_file() 

    async def asyncTearDown(self):  # Use async tearDown
        await aio_os.remove(self.file_name)

    async def create_file(self):
        async with aiofiles.open(self.file_name, 'w'):
            pass

    def append_logs(self):
        entries = [("add 1", 1), ("rem 1", 2), ("sub 2", 3)]
        for entry in entries:
            self.logger.append(entry)
        return entries

    async def test_append_logs(self): # Make tests async
        entries = self.append_logs()
        stored = self.logger.get(0, 3)
        for i in range(3):
            self.assertEqual(entries[i][0], stored[i][0])
            self.assertEqual(entries[i][1], stored[i][1])

        self.assertEqual(self.logger.length(), 3)

    async def test_truncate_logs(self): # Make tests async
        self.append_logs()
        self.logger.truncate(3)
        self.assertEqual(self.logger.length(), 2)
        with self.assertRaises(RaftLogException):
            self.logger.truncate(-1)

    async def test_commit_logs(self): # Make tests async
        entries = self.append_logs()
        self.assertEqual(self.logger.commit_len, 0)
        await self.logger.commit() 
        self.assertEqual(self.logger.commit_len, 3)
        stored = self.logger.get(0, 3)
        for i in range(3):
            self.assertEqual(entries[i][0], stored[i][0])
            self.assertEqual(entries[i][1], stored[i][1])
        self.assertEqual(self.logger.length(), 3)


if __name__ == "__main__":
    unittest.main()