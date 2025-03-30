You will be given instructions, a task, and responses, our goal is to answer the following questions:

For Response A (the first response),

* Truthfulness and Correctness
* Instruction Following
* Able To Run Code

For Response B (the second response),

* Truthfulness and Correctness
* Instruction Following
* Able To Run Code

Conversation Classifications

Which Response is better?

Explaination

-------------------------------------------------------

Instructions:

-------------------------------------------------------

Project Blackhat Instructions
Loom Video:
https://www.loom.com/share/8237c34fed5c4d82a6c696c844a907ae?sid=b52cc5dc-51c8-4aebb87e-b5a90b457cb6
In this task, you will be rating and comparing two responses that were generated from the same
coding related prompt by an AI chatbot.
The form is structured in four sections:
1. You will be shown two different responses to the prompt, and asked if you are able to
directly attempt to run and test the code blocks present
2. You will be asked to rate the correctness of both responses individually.
3. You will be asked to rate how well both responses follow the instructions given in the
prompt
4. You will then provide a rating on the relative quality of the two responses.
Important notes:
● Questions come with detailed instructions. Please read these carefully. Many questions
require explanations depending on the response.
● Some questions require explanations of issues that were found, if any. Aim to write
reasonably concise, but not overly generic explanations that would allow a skilled
programmer to identify and remedy the problem. Expect to write 1-2 sentences on
average.
Out of scope items:
If a prompt is out of scope (e.g. not code related), please select "Cannot Assess" in section 3,
and explain why it is out of scope. You can select the other answers arbitrarily; they will be
filtered out of the metric calculation.
Skipping items:
You should only rate items where you are familiar with the subject material and very confident
that the assessments you’re making are accurate. If you are completely unfamiliar with the
programming language, unable to assess the correctness of responses, or unable to confidently
compare the responses in a reasonable amount of time (~30 minutes), skip the item.
Assessing Correctness:
It is very important to be confident that the ratings you’re providing are accurate. Many aspects
of the rating task are very subtle and nuanced, where relatively small differences between
responses are crucially important, or very reasonable sounding explanations are not factual.
Even if at first glance a response seems perfectly appropriate, it is still important to
● Explicitly check each claim and
● Run code blocks yourself (when appropriate and possible) to verify the code runs and
works as expected
Rating Task
The primary focus of this rating task is on the correctness of the model responses, and how
well the responses follow instructions. Here, correctness refers both to the
truthfulness/factuality of any claim made in the response and the functionality of any code
provided. Instruction following refers to how well the response addresses the goals and
questions, and requirements of the prompt. It is your job to:
(a) Explicitly research and check these textual claims and
(b) Run and inspect the output of any code provided (where applicable) to confirm its
executability and functionality.
You will likely need to utilize google search, stack overflow, documentation, or online code
executors/compilers (e.g., jsfiddle, colab, programiz, etc.) to confirm that a response is
reasonable and that your rating is accurate.
The rating task consists of three parts:
1. Rate the correctness of each of the two responses individually (single-sided).
2. Rate how well each of the two responses follow instructions given in the prompt (singlesided).
3. Rate the relative quality of each response in a side-by-side score.
Task Details:
(1) Code Response Executability:
Are you able to run code provided in the responses?
● Options: Yes-Fully, Yes-Partially, No, No Code Present
● Instructions: Run all code (snippets, functions, programs, etc.) provided in either of the
responses, to check both its executability and its correctness.
○ This may not always be possible. For instance, the code may only make sense
embedded inside a larger program, or it may require some external file/API
dependency for which no execution sandbox is readily available. If the code
cannot be executed, select “No”.
○ Some responses contain multiple code blocks. If you can run some, but not all of
these, answer “Yes-Partially”. Otherwise, answer “Yes-Fully”.
○ Note: This question is not asking about the correctness of the code, only if there
is enough contextual information to test it yourself.
● Explanation: If you answer “Yes-Partially” or “No”, an explanation is required for what
code you were not able to run, and why.
(2) Single-Sided Instruction Following:
Did the response follow the instructions it was given in the prompt (both explicit and
implicit)?
● Options: No Issues, Minor Issue(s), Major Issue(s), N/A
● Instructions: focus on whether the response reflects the instructions and goals of the
prompt, not on truthfulness or correctness issues (e.g., bad code, poor explanation) –
those are rated below. Use the following rubric:
○ No Issues: All prompt instructions were followed; response delivered fully on the
tasks of the prompt.
○ Minor Issue(s): The response addressed most of the instructions or goal(s) of the
prompt, but missed or misinterpreted some small parts. A user would still be
reasonably satisfied.
■ Example: a response that describes the right API but assumes a slightly
different use-case than what the user articulates.
○ Major Issue(s): Response missed key components of the prompt, rendering it
unhelpful to the user.
■ Examples include: a response that discusses a different programming
language or library than what the user asked about, or misses a key
requirement of the code to be generated.
○ N/A - Not Applicable: There are no explicit or implicit instructions to follow in the
prompt or the response is canned (e.g. the model states it cannot do it).
● Explanation: required if issues are found. Describe what aspects of the prompt the
response missed or misinterpreted.
(3) Single-Sided Correctness:
Is the response truthful and correct?
● Options: No Issues, Minor Issue(s), Major Issue(s), Cannot Assess, N/A
● Instructions: identify the correctness of any claims in the explanation and whether the
code (if any) is correct, executable, functional, and useful. Please take up to 30 minutes
to research information across both responses, and explicitly run code snippets as
needed and where appropriate. Use the following rubric:
○ No Issues: All claims in both the explanation and any code comments are factual
and accurate; the code (if any) is functional, safe, and useful.
○ Minor Issues(s): either or both of the following are true:
■ Text: primary claims (central to addressing the prompt) are factual /
accurate; secondary claims contain meaningful inaccuracies (or
unfounded claims).
● /Examples include: an otherwise correct explanation of a library
that uses an incorrect link, or a description of a system that
misconstrues a small detail of its design.
■ Code: has minor problems where the main functionality of the code is
correct; e.g., it fails to handle an edge case, or is correct but has
misleading comments.
○ Major Issues(s): either or both of the following are true:
■ Text: primary claims contain meaningful inaccuracies (or unfounded
claims), such that the response is not helpful to the user.
● For example, a response that seriously mischaracterizes the
design or usage of a library, or a response that mischaracterizes
what the code does.
■ Code: has one or more of the following problems:
● Executability: the program does not compile or run and would
require substantial effort to repair.
● Functionality: The code does not, or will not, produce the proper
intended output or is broken in a logical/functional fashion.
● Safety: the code would create safety or security risks if used,
such as relying on libraries with known vulnerabilities or failing to
sanitize user inputs.
○ Do not use this to flag responses that make simplifying
assumptions that a user would reasonably be expected to
notice and improve, such as using a hard-coded password
in a clearly visible location.
● Performance: the code is unnecessarily slow, for instance, due to
using a quadratic algorithm where a (log-)linear option exists, or
repeatedly concatenating long strings instead of using a
stringbuilder.
● Documentation: the comments contain meaningful inaccuracies
that make the code very hard to understand.
● Keep in mind that the code may be functional for the prompter,
even if it does not compile or run on your setup. For instance, a
response that points to a file only accessible to the prompter, or
provides a partial program based on the context provided by the
prompter should not be marked as non-functional unless it
contains errors that would (likely) manifest in the prompter’s
programming context.
○ Cannot Assess: Cannot determine validity of claims made in the response.
Select this option if properly researching the claims in the response would take
>30 minutes.
○ N/A - Not Applicable: No explicit or implicit claims are made in the response and
it does not include code. Use for this punts (e.g., “As an AI model I am not
capable of responding to this type of question”)
● Explanation: Required if issues are found. Describe all issues. Where possible,
categorize code-related issues based on the type of issue (functionality, safety,
performance, documentation).
(4) Side-by-Side (SxS) Comparison
SxS Score
● Options: Rate your preference between the two responses on a scale from 1 to 7, where
1 means response A is much better than B, 7 means response B is much better than A,
and 4 is neutral.
● Instructions: You should prefer the response that would be more helpful to the user. This
is mainly a function of how correct the response is and how well it followed instructions.
In general, correctness should be the primary consideration and instruction following
secondary, but there may be scenarios where the less correct response is the better
one. Use your best judgment.
○ If the two responses are equal in terms of correctness and instruction following,
you may want to consider other factors such as verbosity or style:
■ Verbosity: Is the length of the response (both the code and non-code
portions) appropriate? The response should include all essential
information, while avoiding excessive additional details. Generally, a
succinct response should be preferred over a verbose one (all else being
equal), but this can depend on preference and context.
■ Style: Does the response use high-quality prose that’s well-organized and
easy to read, and whether the included code, if any, is reasonably
formatted and includes sufficient and accurate documentation
● Explanation: Always required. Briefly explain the most important considerations in your
indicated preference. Relate your motivation to the answers provided above.

--------------------------------------------------

Task:

Below is the code for multiple files from a code repository. Each file begins with "path:" followed by the path to the code file within the repository. The contents of each file appear below the filepath. The end of each file is marked with "[EOD]".

The final code file has a missing section marked with "[FILL IN]". Your task is to generate the correct code for the missing section. Respond only with code that should go in the missing section enclosed in a Markdown code block. The code you generate should match the formatting of the existing code in the file.

path: wconv/wconv/__init__.py

name = 'wconv'


class WConvException(Exception):
    '''
    Custom exception class.
    '''

[EOD]
path: wconv/tests/test_sid.py

#!/usr/bin/python3

import pytest
import wconv.sid as s

from_base64_format = 'base64, sid_value, trustee'
from_base64_tests = [
    ('AQIAAAAAAAUgAAAAIAIAAA==', 'S-1-5-32-544', 'BUILTIN_ADMINISTRATORS'),
    ('AQUAAAAAAAUVAAAAsexT/iL5hu1Kf3av9QEAAA==', 'S-1-5-21-4266912945-3985045794-2943778634-501', 'GUEST'),
    ('AQUAAAAAAAUVAAAAsexT/iL5hu1Kf3avFTcAAA==', 'S-1-5-21-4266912945-3985045794-2943778634-14101', None),
]


@pytest.mark.parametrize(from_base64_format, from_base64_tests)
def test_sid_from_base64(base64, sid_value, trustee):
    sid = s.SecurityIdentifier.from_b64(base64)
    assert sid.formatted_sid == sid_value
    assert sid.well_known == trustee


to_base64_format = 'sid_value, base64'
to_base64_tests = [
    ('S-1-5-32-544', 'AQIAAAAAAAUgAAAAIAIAAA=='),
    ('S-1-5-21-4266912945-3985045794-2943778634-501', 'AQUAAAAAAAUVAAAAsexT/iL5hu1Kf3av9QEAAA=='),
    ('S-1-5-21-4266912945-3985045794-2943778634-14101', 'AQUAAAAAAAUVAAAAsexT/iL5hu1Kf3avFTcAAA=='),
]


@pytest.mark.parametrize(to_base64_format, to_base64_tests)
def test_sid_to_base64(sid_value, base64):
    sid = s.SecurityIdentifier.from_formatted(sid_value)
    b64 = sid.to_b64()
    assert b64 == base64


from_hex_format = 'hex_string, sid_value, trustee'
from_hex_tests = [
    ('01020000000000052000000020020000', 'S-1-5-32-544', 'BUILTIN_ADMINISTRATORS'),
    ('010500000000000515000000b1ec53fe22f986ed4a7f76aff5010000', 'S-1-5-21-4266912945-3985045794-2943778634-501', 'GUEST'),
    ('010500000000000515000000b1ec53fe22f986ed4a7f76af15370000', 'S-1-5-21-4266912945-3985045794-2943778634-14101', None),
]


@pytest.mark.parametrize(from_hex_format, from_hex_tests)
def test_sid_from_hex(hex_string, sid_value, trustee):
    sid = s.SecurityIdentifier.from_hex(hex_string)
    assert sid.formatted_sid == sid_value
    assert sid.well_known == trustee

[EOD]
path: wconv/wconv/ace.py

#!/usr/bin/python3

from termcolor import cprint
from wconv import WConvException


ACE_TYPES = {
    "A": "ACCESS_ALLOWED",
    "D": "ACCESS_DENIED",
    "OA": "ACCESS_ALLOWED_OBJECT",
    "OD": "ACCESS_DENIED_OBJECT",
    "AU": "SYSTEM_AUDIT",
    "AL": "SYSTEM_ALARM",
    "OU": "SYSTEM_AUDIT_OBJECT",
    "OL": "SYSTEM_ALARM_OBJECT"
}

ACE_FLAGS = {
    "CI": "CONTAINER_INHERIT",
    "OI": "OBJECT_INHERIT",
    "NP": "NO_PROPAGATE_INHERIT",
    "IO": "INHERIT_ONLY",
    "ID": "INHERITED",
    "SA": "SUCCESSFUL_ACCESS",
    "FA": "FAILED_ACCESS"
}

GENERIC_PERMISSIONS = {
    "GA": "GENERIC_ALL",
    "GX": "GENERIC_EXECUTE",
    "GW": "GENERIC_WRITE",
    "GR": "GENERIC_READ",

    "SD": "DELETE",
    "RC": "READ_CONTROL",
    "WD": "WRITE_DAC",
    "WO": "WRITE_OWNER"
}

PERMISSIONS_FILE = {
    "CC": "READ",
    "DC": "WRITE",
    "LC": "APPEND",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDED_ATTRIBUTES",
    "WP": "EXECUTE",
    "DT": "MEANINGLESS",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_DIRECTORY = {
    "CC": "LIST",
    "DC": "ADD_FILE",
    "LC": "ADD_SUB_DIR",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDED_ATTRIBUTES",
    "WP": "TRAVERSE",
    "DT": "DELETE_CHILD",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_FILE_MAP = {
    "CC": "FILE_MAP_COPY",
    "DC": "FILE_MAP_WRITE",
    "LC": "FILE_MAP_READ",
    "SW": "FILE_MAP_EXECUTE",
    "RP": "FILE_MAP_EXTEND_MAX_SIZE",
    "WP": "SECTION_MAP_EXECUTE_EXPLICIT"
}

PERMISSIONS_REGISTRY = {
    "CC": "QUERY",
    "DC": "SET",
    "LC": "CREATE_SUB_KEY",
    "SW": "ENUM_SUB_KEY",
    "RP": "NOTIFY",
    "WP": "CREATE_LINK"
}

PERMISSIONS_SERVICE_CONTROL = {
    "CC": "CONNECT",
    "DC": "CREATE_SERVICE",
    "LC": "ENUM_SERVICE",
    "SW": "LOCK",
    "RP": "QUERY_LOCK",
    "WP": "MODIFY_BOOT_CFG"
}

PERMISSIONS_SERVICE = {
    "CC": "QUERY_CONFIG",
    "DC": "CHANGE_CONFIG",
    "LC": "QUERY_STATISTIC",
    "SW": "ENUM_DEPENDENCIES",
    "RP": "START",
    "WP": "STOP",
    "DT": "PAUSE",
    "LO": "INTERROGATE",
    "CR": "USER_DEFINIED"
}

PERMISSIONS_PROCESS = {
    "CC": "TERMINATE",
    "DC": "CREATE_THREAD",
    "LC": "SET",
    "SW": "VM_OPERATE",
    "RP": "VM_READ",
    "WP": "VM_WRITE",
    "DT": "DUP_HANDLE",
    "LO": "CREATE_PROCESS",
    "CR": "SET_QUOTA"
}

PERMISSIONS_THREAD = {
    "CC": "TERMINATE",
    "DC": "SUSPEND",
    "LC": "ALERT",
    "SW": "GET_CONTEXT",
    "RP": "SET_CONTEXT",
    "WP": "SET_INFO",
    "DT": "QUERY_INFO",
    "LO": "SET_TOKEN",
    "CR": "IMPERSONATE"
}

PERMISSIONS_WINDOW_STATION = {
    "CC": "ENUM_DESKTOPS",
    "DC": "READ_ATTRIBUTE",
    "LC": "CLIPBOARD",
    "SW": "CREATE_DESKTOP",
    "RP": "WRITE_ATTRIBUTE",
    "WP": "GLOBAL_ATOMS",
    "DT": "EXIT_WINDOWS",
    "LO": "",
    "CR": "ENUM_WINSTA"
}

PERMISSIONS_DESKTOP = {
    "CC": "READ_OBJECTS",
    "DC": "CREATE_WINDOW",
    "LC": "CREATE_MENU",
    "SW": "HOOK_CONTROL",
    "RP": "JOURNAL_RECORD",
    "WP": "JOURNAL_PLAYBACK",
    "DT": "ENUM",
    "LO": "WRITE_OBJECTS",
    "CR": "SWITCH_DESKTOP"
}

PERMISSIONS_PIPE = {
    "CC": "READ",
    "DC": "WRITE",
    "LC": "CREATE_INSTANCE",
    "SW": "READ_EXTENDED_ATTRIBUTES",
    "RP": "WRITE_EXTENDEN_ATTRIBUTES",
    "WP": "EXECUTE",
    "DT": "DELETE",
    "LO": "READ_ATTRIBUTES",
    "CR": "WRITE_ATTRIBUTES"
}

PERMISSIONS_TOKEN = {
    "CC": "ASSIGN_PRIMARY",
    "DC": "DUPLICATE",
    "LC": "IMPERSONATE",
    "SW": "QUERY",
    "RP": "QUERY_SOURCE",
    "WP": "ADJUST_PRIVELEGES",
    "DT": "ADJUST_GROUPS",
    "LO": "ADJUST_DEFAULT",
    "CR": "ADJUST_SESSION"
}

GROUPED_PERMISSIONS = {
    "FA": "READ_CONTROL,DELETE,WRITE_DAC,WRITE_OWNER,SYNCHRONIZE,READ,WRITE,APPEND,READ_EXTENDED_ATTRIBUTES, \
WRITE_EXTENDED_ATTRIBUTES,EXECUTE,MEANINGLESS,READ_ATTRIBUTES,WRITE_ATTRIBUTES",
    "FR": "READ_CONTROL,READ,READ_ATTRIBUTES,READ_EXTENDED_ATTRIBUES,SYNCHRONIZE",
    "FW": "READ_CONTROL,WRITE,WRITE_ATTRIBUTES,WRITE_EXTENDED_ATTRIBUES,APPEND,SYNCHRONIZE",
    "FX": "READ_CONTROL,READ_ATTRIBUTES,EXECUTE,SYNCHRONIZE",
    "KA": "READ_CONTROL,DELETE,WRITE_DAC,WRITE_OWNER,QUERY,SET,CREATE_SUB_KEY,ENUM_SUB_KEYS,NOTIFY,CREATE_LINK",
    "KR": "READ_CONTROL,QUERY,ENUM_SUB_KEYS,NOTIFY",
    "KW": "READ_CONTROL,SET,CREATE_SUB_KEY",
    "KE": "READ_CONTROL,QUERY,ENUM_SUB_KEYS,NOTIFY"
}

TRUSTEES = {
    'AN': 'Anonymous',
    'AO': 'Account Operators',
    'AU': 'Authenticated Users',
    'BA': 'Administrators',
    'BG': 'Guests',
    'BO': 'Backup Operators',
    'BU': 'Users',
    'CA': 'Certificate Publishers',
    'CD': 'Certificate Services DCOM Access',
    'CG': 'Creator Group',
    'CO': 'Creator Owner',
    'DA': 'Domain Admins',
    'DC': 'Domain Computers',
    'DD': 'Domain Controllers',
    'DG': 'Domain Guests',
    'DU': 'Domain Users',
    'EA': 'Enterprise Admins',
    'ED': 'Enterprise Domain Controllers',
    'RO': 'Enterprise Read-Only Domain Controllers',
    'PA': 'Group Policy Admins',
    'IU': 'Interactive Users',
    'LA': 'Local Administrator',
    'LG': 'Local Guest',
    'LS': 'Local Service',
    'SY': 'Local System',
    'NU': 'Network',
    'LW': 'Low Integrity',
    'ME': 'Medium Integrity',
    'HI': 'High Integrity',
    'SI': 'System Integrity',
    'NO': 'Network Configuration Operators',
    'NS': 'Network Service',
    'PO': 'Printer Operators',
    'PS': 'Self',
    'PU': 'Power Users',
    'RS': 'RAS Servers',
    'RD': 'Remote Desktop Users',
    'RE': 'Replicator',
    'RC': 'Restricted Code',
    'RU': 'Pre-Win2k Compatibility Access',
    'SA': 'Schema Administrators',
    'SO': 'Server Operators',
    'SU': 'Service',
    'WD': 'Everyone',
    'WR': 'Write restricted Code',
}

ACCESS_MASK_HEX = dict([
    (0x10000000, 'GA'),
    (0x20000000, 'GX'),
    (0x40000000, 'GW'),
    (0x80000000, 'GR'),

    (0x00010000, 'SD'),
    (0x00020000, 'RC'),
    (0x00040000, 'WD'),
    (0x00080000, 'WO'),

    (0x00000001, 'CC'),
    (0x00000002, 'DC'),
    (0x00000004, 'LC'),
    (0x00000008, 'SW'),
    (0x00000010, 'RP'),
    (0x00000020, 'WP'),
    (0x00000040, 'DT'),
    (0x00000080, 'LO'),
    (0x00000100, 'CR'),

    (0x000f01ff, 'FA'),
    (0x00020089, 'FR'),
    (0x00020116, 'FW'),
    (0x000200a0, 'FX'),

    (0x000f003f, 'KA'),
    (0x00020019, 'KR'),
    (0x00020006, 'KW'),
    (0x00020019, 'KE')
])

ACCESS_MASK_HEX_REVERSE = dict([
    ('GA', 0x10000000),
    ('GX', 0x20000000),
    ('GW', 0x40000000),
    ('GR', 0x80000000),

    ('SD', 0x00010000),
    ('RC', 0x00020000),
    ('WD', 0x00040000),
    ('WO', 0x00080000),

    ('CC', 0x00000001),
    ('DC', 0x00000002),
    ('LC', 0x00000004),
    ('SW', 0x00000008),
    ('RP', 0x00000010),
    ('WP', 0x00000020),
    ('DT', 0x00000040),
    ('LO', 0x00000080),
    ('CR', 0x00000100),

    ('FA', 0x000f01ff),
    ('FR', 0x00020089),
    ('FW', 0x00020116),
    ('FX', 0x000200a0),

    ('KA', 0x000f003f),
    ('KR', 0x00020019),
    ('KW', 0x00020006),
    ('KE', 0x00020019)
])

PERM_TYPE_MAPPING = {
    'file':             dict(GENERIC_PERMISSIONS, **PERMISSIONS_FILE),
    'directory':        dict(GENERIC_PERMISSIONS, **PERMISSIONS_DIRECTORY),
    'file_map':         dict(GENERIC_PERMISSIONS, **PERMISSIONS_FILE_MAP),
    'registry':         dict(GENERIC_PERMISSIONS, **PERMISSIONS_REGISTRY),
    'service':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_SERVICE),
    'service_control':  dict(GENERIC_PERMISSIONS, **PERMISSIONS_SERVICE_CONTROL),
    'process':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_PROCESS),
    'thread':           dict(GENERIC_PERMISSIONS, **PERMISSIONS_THREAD),
    'window_station':   dict(GENERIC_PERMISSIONS, **PERMISSIONS_WINDOW_STATION),
    'desktop':          dict(GENERIC_PERMISSIONS, **PERMISSIONS_DESKTOP),
    'pipe':             dict(GENERIC_PERMISSIONS, **PERMISSIONS_PIPE),
    'token':            dict(GENERIC_PERMISSIONS, **PERMISSIONS_TOKEN),
}


def get_permission_dict(permission_type):
    '''
    The meaning of permission shortnames like 'CC' change depending on the resource
    they are assigned to. This function returns the corresponding dictionary for
    the requested permission type.

    Parameters:
        permission_type         (string)        Permission type (file, service, ...)

    Returns:
        permission_dict         (dict)          Dictionary containing permission map
    '''
    try:
        mapping = PERM_TYPE_MAPPING[permission_type]
        return mapping

    except KeyError:
        raise WConvException(f"get_permissions_dict(... - Unknown permission type '{permission_type}'")


class Ace:
    '''
    The Ace class represents a single ACE entry inside a SDDL string.
    '''
    ace_everyone = '(A;;GAGRGWGXRCSDWDWOSSCCDCLCSWRPWPDTLOCR;;;WD)'
    ace_anonymous = '(A;;GAGRGWGXRCSDWDWOSSCCDCLCSWRPWPDTLOCR;;;AN)'

    def __init__(self, ace_type, ace_flags, permissions, object_type, inherited_object_type, trustee, numeric):
        '''
        The init function takes the six different ACE components and constructs an object out of them.

        Parameters:
            ace_type        (string)            ace_type according to the sddl specifications
            ace_flags       (list[string])      ace_flags according to the sddl specifications
            permissions     (list[string])      permissions defined inside the ACE
            object_type     (string)            object_type according to the sddl specifications
            i_object_type   (string)            inherited_object_type according to the sddl specifications
            trustee         (string)            trustee the ACE applies to
            numeric         (int)               Integer ace value

        Returns:
            ace_object      (Ace)               New generated ACE object
        '''
        self.ace_type = ace_type
        self.ace_flags = ace_flags
        self.permissions = permissions
        self.object_type = object_type
        self.inherited_object_type = inherited_object_type
        self.trustee = trustee
        self.numeric = numeric

    def __str__(self):
        '''
        Outputs a simple string represenation of the ACE. Only used for debugging purposes.

        Paramaters:
            None

        Returns:
            None
        '''
        if self.ace_type:
            result = f'ACE Type:\t {self.ace_type}\n'

        if self.ace_trustee:
            result += f'Trustee:\t {self.trustee}\n'

        if self.permissions:
            result += 'Permissions:\n'
            for perm in self.permissions:
                result += f'\t\t+ {perm}\n'

        if self.ace_flags:
            result += 'ACE Flags:\n'
            for flag in self.ace_flags:
                result += f'\t\t+ {flag}\n'

        return result[:-1]

    def pretty_print(self, indent=' ', verbose=False):
        '''
        Prints some formatted and colored output that represents the ACE. Probably not really
        ideal to be placed inside a library, but for now we can live with that.

        Parameters:
            indent          (string)            Spaces after the '[+]' prefix
            verbose         (boolean)           Decides if ACE flags are printed

        Returns:
            None
        '''
        if self.ace_type:
            cprint(f'[+]{indent}ACE Type:\t', 'blue', end='')
            cprint(self.ace_type, 'yellow')

        if self.trustee:
            cprint(f'[+]{indent}Trustee:\t', 'blue', end='')
            cprint(self.trustee, 'yellow')

        if self.numeric:
            cprint(f'[+]{indent}Numeric:\t', 'blue', end='')
            cprint('0x{:08x}'.format(self.numeric), 'yellow')

        if verbose:
            if self.ace_flags:

                cprint(f'[+]{indent}ACE Flags:\t', 'blue')
                for flag in self.ace_flags:
                    cprint('[+]', 'blue', end='')
                    cprint(f'{indent}\t\t+ {flag}', 'yellow')

        if self.permissions:

            cprint(f'[+]{indent}Permissions:\t', 'blue')
            for perm in self.permissions:
                cprint('[+]', 'blue', end='')
                cprint(f'{indent}\t\t+ {perm}', 'yellow')

    def clear_parentheses(ace_string):
        '''
        Removes the opening and closing parantheses from an ACE string (if present).

        Paramaters:
            ace_string      (string)            ACE string to operate on

        Returns:
            ace_string      (string)            ACE string without parentheses
        '''
        if ace_string[0] == '(':
            ace_string = ace_string[1:]

        if ace_string[-1] == ')':
            ace_string = ace_string[:-1]

        return ace_string

    def get_ace_flags(ace_flag_string):
        '''
        Parses the flag-portion of an ACE string and returns a list of the corresponding
        ACE flags.

        Paramaters:
            ace_flag_string (string)            String containing the ACE flags

        Returns:
            ace_flags       (list[string])      List containing the parsed ACE flags
        '''
        ace_flags = []

        for ctr in range(0, len(ace_flag_string), 2):

            try:
                ace_flag = ace_flag_string[ctr:ctr+2]
                ace_flag = ACE_FLAGS[ace_flag]
                ace_flags.append(ace_flag)

            except KeyError:
                raise WConvException(f"get_ace_flags(... - Unknown ACE flag '{ace_flag}'.")

        return ace_flags

    def get_ace_permissions(ace_permission_string, perm_type='file'):
        '''
        Takes the ACE portion containing the permission and returns a list of the corresponding parsed
        permissions.

        Paramaters:
            ace_permission_string   (string)        String containing the ACE permissions
            perm_type               (string)        Permission type (file, service, ...)

        Returns:
            permissions             (list[string])  List of corresponding permissions
        '''
        permissions = []
        perm_dict = get_permission_dict(perm_type)

        for ctr in range(0, len(ace_permission_string), 2):

            permission = ace_permission_string[ctr:ctr+2]

            try:

                if permission in GROUPED_PERMISSIONS:
                    permission = GROUPED_PERMISSIONS[permission]
                    permission = permission.split(",")
                    permissions += permission
                else:
                    permission = perm_dict[permission]
                    permissions.append(permission)

            except KeyError:
                raise WConvException(f"from_string(... - Unknown permission name '{permission}'.")

        return permissions

    def get_ace_numeric(ace_permission_string):
        '''
        Takes the ACE portion containing the permission and returns the corresponding integer value.

        Paramaters:
            ace_permission_string   (string)        String containing the ACE permissions

        Returns:
            ace_int                 (int)           Corresponding integer value
        '''
        ace_int = 0

        for ctr in range(0, len(ace_permission_string), 2):

            permission = ace_permission_string[ctr:ctr+2]

            try:
                ace_int += ACCESS_MASK_HEX_REVERSE[permission]

            except KeyError:
                raise WConvException(f"from_string(... - Unknown permission name '{permission}'.")

        return ace_int

    def from_string(ace_string, perm_type='file'):
        '''
        Parses an ace from a string in SDDL representation (e.g. A;OICI;FA;;;BA).

        Parameters:
            ace_string      (string)            ACE string in sddl format
            perm_type       (string)            Object type the sddl applies to (file, service, ...)

        Returns:
            ace_object      (Ace)
        '''
        ace_string = Ace.clear_parentheses(ace_string)

        ace_split = ace_string.split(';')
        if len(ace_split) != 6:
            raise WConvException(f"from_string(... - Specified value '{ace_string}' is not a valid ACE string.")

        try:
            ace_type = ACE_TYPES[ace_split[0]]
        except KeyError:
            raise WConvException(f"from_string(... - Unknown ACE type '{ace_split[0]}'.")

        ace_flags = Ace.get_ace_flags(ace_split[1])
        permissions = Ace.get_ace_permissions(ace_split[2], perm_type)
        ace_int = Ace.get_ace_numeric(ace_split[2])

        object_type = ace_split[3]
        inherited_object_type = ace_split[4]

        trustee = ace_split[5]
        if trustee in TRUSTEES:
            trustee = TRUSTEES[trustee]

        return Ace(ace_type, ace_flags, permissions, object_type, inherited_object_type, trustee, ace_int)

    def from_int(integer, perm_type='file'):
        '''
        Parses an ace from an integer value in string representation.

        Parameters:
            integer         (string)            Integer value as string (hex also allowed)
            perm_type       (string)            Object type the sddl applies to (file, service, ...)

        Returns:
            ace_object      (Ace)
        '''
        try:
            ace_int = int(integer, 0)
        except ValueError:
            raise WConvException(f"from_int(... - Specified value '{integer}' is not an integer.")

        perm_dict = get_permission_dict(perm_type)
        permissions = []

        for key, value in ACCESS_MASK_HEX.items():

            if key & ace_int:

                try:
                    permission = perm_dict[value]
                    permissions.append(permission)

                except KeyError:
                    # Ignore matches on grouped permissions like FA, FR, FW...
                    pass

        return Ace(None, None, permissions, None, None, None, ace_int)

    def toggle_permission(integer, permissions):
        '''
        Takes an ace in integer format and toggles the specified permissions on it.

        Parameters:
            integer         (string)            Integer value as string (hex also allowed)
            permissions     (list[string])      List of permission to toggle (GA, GR, GW, GE, CC, ...)

        Returns:
            integer         (string)            Resulting ace value as integer in hex format
        '''
        try:
            ace_int = int(integer, 0)
        except ValueError:
            raise WConvException(f"from_int(... - Specified value '{integer}' is not an integer.")

        for permission in permissions:

            try:
                hex_value = ACCESS_MASK_HEX_REVERSE[permission]
                ace_int = ace_int ^ hex_value

            except KeyError:
                raise WConvException(f"toggle_permission(... - Unknown permission name '{permission}'")

        return "0x{:08x}".format(ace_int)

[EOD]
path: wconv/requirements.txt

termcolor

[EOD]
path: wconv/tests/test_uac.py

#!/usr/bin/python3

import pytest
import wconv.uac as u

constructor_format = 'uac_value, flags'
constructor_tests = [
    ('532480', ['SERVER_TRUST_ACCOUNT', 'TRUSTED_FOR_DELEGATION']),
    ('66082', ['ACCOUNTDISABLE', 'PASSWD_NOTREQD', 'NORMAL_ACCOUNT', 'DONT_EXPIRE_PASSWORD']),
    ('4096', ['WORKSTATION_TRUST_ACCOUNT']),
]


@pytest.mark.parametrize(constructor_format, constructor_tests)
def test_uac_constructor(uac_value, flags):
    uac = u.UserAccountControl(uac_value)
    assert uac.flags == flags


toggle_format = 'initial, toggle_list, flags, numeric'
toggle_tests = [
    ('0', ['SERVER_TRUST_ACCOUNT', 'TRUSTED_FOR_DELEGATION'],
        ['SERVER_TRUST_ACCOUNT', 'TRUSTED_FOR_DELEGATION'], 532480),

    ('66082', ['ACCOUNTDISABLE', 'PASSWD_NOTREQD'],
        ['NORMAL_ACCOUNT', 'DONT_EXPIRE_PASSWORD'], 66048),

    ('4096', ['SERVER_TRUST_ACCOUNT'],
        ['WORKSTATION_TRUST_ACCOUNT', 'SERVER_TRUST_ACCOUNT'], 12288),
]


@pytest.mark.parametrize(toggle_format, toggle_tests)
def test_uac_toggle(initial, toggle_list, flags, numeric):
    uac = u.UserAccountControl(initial)
    uac.toggle_flag(toggle_list)
    assert uac.flags == flags
    assert uac.uac_value == numeric

[EOD]
path: wconv/wconv/uac.py

#!/usr/bin/python3

from termcolor import cprint
from wconv import WConvException

UAC_DICT = dict([
    (0x00000001, "SCRIPT"),
    (0x00000002, "ACCOUNTDISABLE"),
    (0x00000008, "HOMEDIR_REQUIRED"),
    (0x00000010, "LOCKOUT"),
    (0x00000020, "PASSWD_NOTREQD"),
    (0x00000040, "PASSWD_CANT_CHANGE"),
    (0x00000080, "ENCRYPTED_TEXT_PWD_ALLOWED"),
    (0x00000100, "TEMP_DUPLICATE_ACCOUNT"),
    (0x00000200, "NORMAL_ACCOUNT"),
    (0x00000800, "INTERDOMAIN_TRUST_ACCOUNT"),
    (0x00001000, "WORKSTATION_TRUST_ACCOUNT"),
    (0x00002000, "SERVER_TRUST_ACCOUNT"),
    (0x00010000, "DONT_EXPIRE_PASSWORD"),
    (0x00020000, "MNS_LOGON_ACCOUNT"),
    (0x00040000, "SMARTCARD_REQUIRED"),
    (0x00080000, "TRUSTED_FOR_DELEGATION"),
    (0x00100000, "NOT_DELEGATED"),
    (0x00200000, "USE_DES_KEY_ONLY"),
    (0x00400000, "DONT_REQ_PREAUTH"),
    (0x00800000, "PASSWORD_EXPIRED"),
    (0x01000000, "TRUSTED_TO_AUTH_FOR_DELEGATION"),
    (0x04000000, "PARTIAL_SECRETS_ACCOUNT")
])

UAC_DICT_REVERSE = dict([
    ("SCRIPT",                          0x00000001),
    ("ACCOUNTDISABLE",                  0x00000002),
    ("HOMEDIR_REQUIRED",                0x00000008),
    ("LOCKOUT",                         0x00000010),
    ("PASSWD_NOTREQD",                  0x00000020),
    ("PASSWD_CANT_CHANGE",              0x00000040),
    ("ENCRYPTED_TEXT_PWD_ALLOWED",      0x00000080),
    ("TEMP_DUPLICATE_ACCOUNT",          0x00000100),
    ("NORMAL_ACCOUNT",                  0x00000200),
    ("INTERDOMAIN_TRUST_ACCOUNT",       0x00000800),
    ("WORKSTATION_TRUST_ACCOUNT",       0x00001000),
    ("SERVER_TRUST_ACCOUNT",            0x00002000),
    ("DONT_EXPIRE_PASSWORD",            0x00010000),
    ("MNS_LOGON_ACCOUNT",               0x00020000),
    ("SMARTCARD_REQUIRED",              0x00040000),
    ("TRUSTED_FOR_DELEGATION",          0x00080000),
    ("NOT_DELEGATED",                   0x00100000),
    ("USE_DES_KEY_ONLY",                0x00200000),
    ("DONT_REQ_PREAUTH",                0x00400000),
    ("PASSWORD_EXPIRED",                0x00800000),
    ("TRUSTED_TO_AUTH_FOR_DELEGATION",  0x01000000),
    ("PARTIAL_SECRETS_ACCOUNT",         0x04000000)
])


class UserAccountControl:
    '''
    Represents a UserAccountControl entry of Active Directory.
    '''

    def __init__(self, uac_value):
        '''
        Consrutcs a new UserAccountControl object from an UAC integer in string representation.

        Paramaters:
            uac_value           (string)            UAC integer value in string format

        Returns:
            UserAccountControl  (UserAccountControl)
        '''
        try:
            uac_int = int(uac_value, 0)
        except ValueError:
            raise WConvException(f"__init__(... - Specified UAC value '{uac_value}' is not an integer.")

        self.uac_value = uac_int
        self.flags = UserAccountControl.parse_flags(uac_int)

    def __str__(self):
        '''
        Converts a UserAccountControl object into a simple formatted string. Useful for debugging purposes.

        Paramaters:
            None

        Returns:
            result              (string)            UserAccountControl object in string representation
        '''
        result = f'UserAccountControl: {self.uac_value}\n'

        for flag in self.flags:
            result += f'    {flag}\n'

        return result[:-1]

    def pretty_print(self):
        '''
        Prints some formatted and colored information about the UserAccountControl object.

        Parameters:
            None

        Returns:
            None
        '''
        cprint('[+] UserAccountControl:\t', 'blue', end='')
        cprint('{} (0x{:08x})'.format(self.uac_value, self.uac_value), 'yellow')

        for flag in self.flags:
            cprint('[+]\t', 'blue', end='')
            cprint(f'+ {flag}', 'yellow')

    def toggle_flag(self, flags):
        '''
        Toggles the specified UAC flag on the UserAccountControl object.

        Parameters:
            flags           (list[str])         List of flags to enable on the UAC object

        Returns:
            None
        '''
        for flag in flags:

            try:
                numeric = UAC_DICT_REVERSE[flag]
                self.uac_value = self.uac_value ^ numeric
                self.flags = UserAccountControl.parse_flags(self.uac_value)

            except KeyError:
                raise WConvException(f"toggle_flag(... - Specified UAC flag '{flag}' does not exist.")

    def parse_flags(uac_value):
        '''
        Takes an integer UserAccountControl value and returns a formatted string
        containing the corresponding flags.

        Paramaters:
            uac_value       (int)               UserAccountControl value

        Returns:
            flags           (list[string])      List of UAC flags
        '''
        flags = []

        for key, value in UAC_DICT.items():
            if uac_value & key:
                flags.append(value)

        return flags

[EOD]
path: wconv/tests/test_ace.py

#!/usr/bin/python3

import pytest
import wconv.ace as a

from_string_format = 'ace_string, perm_type, ace_type, trustee, numeric, flags, perms'
from_string_tests = [
    ('(A;OICI;SDWD;;;BU)', 'file', 'ACCESS_ALLOWED', 'Users', 0x00050000,
        ['OBJECT_INHERIT', 'CONTAINER_INHERIT'], ['DELETE', 'WRITE_DAC']),

    ('(D;NPFA;GAWP;;;BA)', 'registry', 'ACCESS_DENIED', 'Administrators', 0x10000020,
        ['NO_PROPAGATE_INHERIT', 'FAILED_ACCESS'], ["GENERIC_ALL", "CREATE_LINK"]),

    ('(AU;SAID;CCDC;;;SY)', 'service', 'SYSTEM_AUDIT', 'Local System', 0x00000003,
        ['SUCCESSFUL_ACCESS', 'INHERITED'], ['QUERY_CONFIG', 'CHANGE_CONFIG']),

    ('(AL;IOSA;LCWP;;;BO)', 'token', 'SYSTEM_ALARM', 'Backup Operators', 0x00000024,
        ['INHERIT_ONLY', 'SUCCESSFUL_ACCESS'], ['IMPERSONATE', 'ADJUST_PRIVELEGES'])
]


@pytest.mark.parametrize(from_string_format, from_string_tests)
def test_ace_from_string(ace_string, perm_type, ace_type, trustee, numeric, flags, perms):
    ace = a.Ace.from_string(ace_string, perm_type)
    assert ace.ace_type == ace_type
    assert ace.trustee == trustee
    assert ace.numeric == numeric
    assert ace.ace_flags == flags
    assert ace.permissions == perms


from_int_format = 'ace_int, perm_type, perms'
from_int_tests = [
    ('0x00050000', 'file', ['DELETE', 'WRITE_DAC']),
    ('0x10000020', 'registry', ['GENERIC_ALL', 'CREATE_LINK']),
    ('0x00000003', 'service', ['QUERY_CONFIG', 'CHANGE_CONFIG']),
    ('0x00000024', 'token', ['IMPERSONATE', 'ADJUST_PRIVELEGES'])
]


@pytest.mark.parametrize(from_int_format, from_int_tests)
def test_ace_from_int(ace_int, perm_type, perms):
    ace = a.Ace.from_int(ace_int, perm_type)
    assert ace.numeric == int(ace_int, 16)
    assert ace.permissions == perms


toggle_format = 'initial, toggle_list, permissions, numeric'
toggle_tests = [
    ('0x00000000', ['GA', 'GR'], ['GENERIC_ALL', 'GENERIC_READ'], 0x90000000),
    ('0x90000000', ['GR'], ['GENERIC_ALL'], 0x10000000)
]


@pytest.mark.parametrize(toggle_format, toggle_tests)
def test_ace_toggle(initial, toggle_list, permissions, numeric):
    ace_value = a.Ace.toggle_permission(initial, toggle_list)
    ace = a.Ace.from_int(ace_value)
    assert ace.numeric == numeric
    assert ace.permissions == permissions

[EOD]
path: wconv/wconv/sddl.py

#!/usr/bin/python3

import re

from termcolor import cprint
from wconv import WConvException
from wconv.ace import Ace, TRUSTEES


SDDL_HEADERS = {
    "O": "Owner",
    "G": "Group",
    "D": "DACL",
    "S": "SACL"
}

ACL_FLAGS = {
    "P": "PROTECTED",
    "AI": "ACL_INHERITANCE",
    "AR": "LEGACY_ACL_INHERITANCE"
}


class Sddl:
    '''
    The Sddl class represents a Windows Sddl for an particular object.
    E.g.: D:PAI(D;OICI;FA;;;BG)(A;OICI;FA;;;BA)(A;OICIIO;FA;;;CO)(A;OICI;FA;;;SY)(A;OICI;FA;;;BU)
    '''
    # regex definitions to parse required elements from sddl
    re_owner = re.compile('O:([^:()]+)(?=[DGS]:)')
    re_group = re.compile('G:([^:()]+)(?=[DOS]:)')
    re_acl_type = re.compile('([DS]:(P|AI|AR)*)')
    re_ace = re.compile(r'\((([^\);]*;){5}[^\)]*)\)')

    def __init__(self, owner, group, acl_type, acl_flags, ace_list):
        '''
        The init function takes the different components of a Sddl and creates an object out of
        them. It should not be called directly. Instead, the helper functions 'from_... should
        be used.

        Parameters:
            owner           (string)            Owner of the corresponding object
            group           (string)            Group of the corresponding object
            acl_type        (string)            Only DACL is currently supported
            acl_flags       (list[string])      ACL flags according to the SDDL specification
            ace_list        (list[Ace])         List of Ace objects parsed from the sddl
        '''
        self.owner = owner
        self.group = group
        self.acl_type = acl_type
        self.acl_flags = acl_flags
        self.ace_list = ace_list

    def pretty_print(self, indent=' ', verbose=False):
        '''
        Prints the Sddl and the contained Aces in a formatted and colored format. Not
        ideal for a library, however, currently we can live with it.

        Parameters:
            indent          (string)            Spaces after the '[+]' prefix
            verbose         (boolean)           Decides if ACE flags are printed

        Returns:
            None
        '''
        cprint(f'[+]{indent}ACL Type:\t', 'blue', end='')
        cprint(self.acl_type, 'yellow')

        cprint(f'[+]{indent}Owner:\t', 'blue', end='')
        cprint(self.owner, 'yellow')

        cprint(f'[+]{indent}Group:\t', 'blue', end='')
        cprint(self.group, 'yellow')

        if verbose:
            cprint(f'[+]{indent}ACL Flags:', 'blue')

            for flag in self.acl_flags:
                cprint('[+]', 'blue', end='')
                cprint(f'{indent}\t\t+ {flag}', 'yellow')

        cprint(f'[+]{indent}ACE List:', 'blue')
        cprint('[+] ==================================', 'blue')

        for ace in self.ace_list:
            ace.pretty_print(verbose=verbose, indent=indent + ' '*4)
            cprint('[+] ==================================', 'blue')

    def get_owner(sddl_string):
        '''
        Returns the owner contained inside a SDDL string or None if no owner
        was specified.

        Paramaters:
            sddl_string         (string)        Portion containing the owner is sufficient

        Returns:
            owner               (string)        Object owner or None
        '''
        match = Sddl.re_owner.search(sddl_string)

        if match:

            owner = match.group(1)
            if owner in TRUSTEES:
                owner = TRUSTEES[owner]

        else:
            owner = None

        return owner

    def get_group(sddl_string):
        '''
        Returns the group contained inside a SDDL string or None if no group
        was specified.

        Paramaters:
            sddl_string         (string)        Portion containing the group is sufficient

        Returns:
            group               (string)        Object group or None
        '''
        match = Sddl.re_group.search(sddl_string)

        if match:

            group = match.group(1)
            if group in TRUSTEES:
                group = TRUSTEES[group]

        else:
            group = None

        return group

    def get_acl_flags(acl_flags_string):
        '''
        Takes the SDDL portion behind the 'D:' (acl flags) and returns a list of the corresponding
        contained ACL flags.

        Paramaters:
            acl_flags_strings   (string)        Sring containing the ACL flags ('D:THISONE(')

        Returns:
            acl_flags           (list[string])  List of contained ACL flags
        '''
        acl_flags = []

        if 'P' in acl_flags_string:
            acl_flags.append(ACL_FLAGS['P'])

        if 'AI' in acl_flags_string:
            acl_flags.append(ACL_FLAGS['AI'])

        if 'AR' in acl_flags_string:
            acl_flags.append(ACL_FLAGS['AR'])

        return acl_flags

    def get_ace_list(ace_string, perm_type='file'):
        '''
        Takes the SDDL portion that contains the ACEs and returns a list of corresponding ACE objects.

        Paramaters:
            ace_string          (string)        SDDL portion that contains the ACEs
            perm_type           (string)        Permission type for ACE generation

        Returns:
            ace_list            (list[ACE])     Corresponding list of ACE objects
        '''
        ace_strings = Sddl.re_ace.findall(ace_string)
        ace_strings = list(map(lambda x: x[0], ace_strings))

        ace_list = []
        for ace_string in ace_strings:

            ace = Ace.from_string(ace_string, perm_type=perm_type)
            ace_list.append(ace)

        return ace_list

    def from_string(sddl_string, perm_type='file'):
        '''
        Parses an SDDL string an creates the corresponding Sddl object out of it.

        Parameters:
            sddl_string         (string)        String that represents the sddl
            perm_type           (string)        Type of the corresponding object (file, service, ...)

        Returns:
            sddl_object         (Sddl)
        '''
        # Split sddl header from ace strings
        try:

            header_index = sddl_string.index('(')
            sddl_header_string = sddl_string[:header_index]
            sddl_ace_string = sddl_string[header_index:]

        except ValueError:
            raise WConvException("parse_sddl(... - Input string is no valid SDDL.")

        # Extract the acl type and the corresponding acl flags
        match = Sddl.re_acl_type.search(sddl_header_string)

        if not match:
            raise WConvException("parse_sddl(... - Input string is no valid SDDL.")

        # Save acl type
        acl_type_split = match.group(0).split(':')

        if acl_type_split[0] == 'D':
            acl_type = 'DACL'

        else:
            raise WConvException("parse_sddl(... - Input string describes no DACL. Other formarts are not supported.")

        acl_flags = Sddl.get_acl_flags(acl_type_split[1])
        owner = Sddl.get_owner(sddl_header_string)
        group = Sddl.get_group(sddl_header_string)
        ace_list = Sddl.get_ace_list(sddl_ace_string, perm_type)

        return Sddl(owner, group, acl_type, acl_flags, ace_list)

    def add_everyone(sddl_string):
        '''
        Adds full permissions for everyone on the specified sddl_string.

        Parameters:
            sddl_string         (string)            SDDL string

        Returns:
            sddl_string         (string)            SDDL string with full permissions for everyone
        '''
        return sddl_string + Ace.ace_everyone

    def add_anonymous(sddl_string):
        '''
        Adds full permissions for anonymous on the specified sddl_string.

        Parameters:
            sddl_string         (string)            SDDL string

        Returns:
            sddl_string         (string)            SDDL string with full permissions for anonymous
        '''
        return sddl_string + Ace.ace_anonymous

[EOD]
path: wconv/setup.py

#!/usr/bin/python3

from os.path import expanduser, abspath, dirname, isdir, isfile
from shutil import copy

from setuptools import setup
from setuptools.command.install import install


name = 'wconv'
with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstall(install):
    '''
    Subclass to allow running commands after package installation. Required for setup of the
    completion script.
    '''
    def run(self):
        PostInstall.setup_completion()
        install.run(self)

    def setup_completion():
        '''
        Checks whether the '~/.bash_completion.d' folder exists and copies the autocompletion script
        into it. If the folder does not exist the function just returns. The completion script is
        expected to be sored in the path: {mdoule_path}/{name}/resources/bash_completion.d/{name}

        Parameters:
             None

         Returns:
             None
        '''
        user_home = expanduser("~")
        module_path = abspath(dirname(__file__))

        completion_dir = f'{user_home}/.bash_completion.d/'
        if not isdir(completion_dir):
            return

        completion_file = f'{module_path}/{name}/resources/bash_completion.d/{name}'
        completion_target = f'{completion_dir}/{name}'

        if not isfile(completion_file):
            return

        copy(completion_file, completion_target)


setup(
    url='https://github.com/qtc-de/wconv',
    name=name,
    author='Tobias Neitzel (@qtc_de)',
    version='1.0.2',
    author_email='',

    description='wconv - Converting Windows native formats to human readable form',
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=['wconv'],
    package_data={
                        name: [
                            'resources/*',
                            'resources/bash_completion.d/*',
                        ]
                   },
    install_requires=[
                        'termcolor',
                     ],
    scripts=[
                f'bin/{name}',
            ],
    cmdclass={
                'install': PostInstall,
             },
    classifiers=[
                    'Programming Language :: Python :: 3',
                    'Operating System :: Unix',
                    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                ],
)

[EOD]


path: wconv/tests/test_sddl.py

#!/usr/bin/python3

import pytest
import wconv.sddl as s

from_string_format = 'sddl_string, acl_type, acl_flags, owner, group, numeric_ace_1, numeric_ace_2'
from_string_tests = [
    ('O:BAG:SYD:PAI(D;CI;DCWP;;;BA)(A;OI;RPDT;;;CO)', 'DACL', ['PROTECTED', 'ACL_INHERITANCE'],
        'Administrators', 'Local System', 0x00000022, 0x00000050),

    ('O:BOD:AR(D;CI;GAGR;;;BU)(A;;CC;;;WD)', 'DACL', ['LEGACY_ACL_INHERITANCE'],
        'Backup Operators', None, 0x90000000, 0x00000001),

    ('G:DAD:P(D;CI;WP;;;ED)(D;;DC;;;AN)', 'DACL', ['PROTECTED'],
        None, 'Domain Admins', 0x00000020, 0x00000002),

    ('D:P(D;CI;WPGA;;;ED)(D;;DCGR;;;AN)', 'DACL', ['PROTECTED'],
        None, None, 0x10000020, 0x80000002),
]


@pytest.mark.parametrize(from_string_format, from_string_tests)
def test_sddl_from_string(sddl_string, acl_type, acl_flags, owner, group, numeric_ace_1, numeric_ace_2):
# Tests the correctness of parsing an SDDL string into an `Sddl` object
[FILL IN]
--------------------------------------------------

Response A:
```python
    sddl = s.Sddl.from_string(sddl_string)
    assert sddl.acl_type == acl_type
    assert sddl.acl_flags == acl_flags
    assert sddl.owner == owner
    assert sddl.group == group
    assert sddl.ace_list[0].numeric == numeric_ace_1
    assert sddl.ace_list[1].numeric == numeric_ace_2

```
--------------------------------------------------

Response B:
```python
    sddl = s.Sddl.from_string(sddl_string)
    assert sddl.acl_type == acl_type
    assert sddl.acl_flags == acl_flags
    assert sddl.owner == owner
    assert sddl.group == group
    assert sddl.ace_list[0].numeric == numeric_ace_1
    assert sddl.ace_list[1].numeric == numeric_ace_2
```
--------------------------------------------------
