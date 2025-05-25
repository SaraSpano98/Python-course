"""
Mechanism that restricts objects to attributes listed in '__slots__'.
"""

class MyClassWithSlots:
    __slots__ = ['a']
    def __init__(self):
        self.a = 1

from copy import copy, deepcopy

# Example usage:
obj = MyClassWithSlots()
obj_copy = copy(obj)
obj_deepcopy = deepcopy(obj)