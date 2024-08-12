"""
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, 
even when some of those items were created on a different server or by a different application. 
That is, without any synchronization, two or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each other's toes. 
It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. 
The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed. There are several UUID versions, each with some non-random characteristics in some of the bits. These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.
"""

import uuid
import random

def uuid_str():
    return uuid.uuid5(uuid.NAMESPACE_X500, 'python.org')

print(uuid_str())

def uuid_gen():
    hex = list('abcdefgh1234567890')
    structure = [8, 4, 4, 4, 12]
    uuid = []

    for section in structure:
        for i in range(section):
            uuid.append(random.choice(hex))
            if i == section - 1 and section != 12:
                uuid.append('-')
    return ''.join(uuid)

print(uuid_gen())
