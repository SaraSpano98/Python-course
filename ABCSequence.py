"""
It's a richer interface than the basic sequence.
Extending it generates iter(), contains(), reversed(), index() and count().
Unlike 'abc.Iterable' and 'abc.Collection', it is not a duck type. That is why 'issubclass(MySequence, abc.Sequence)' would return False even if MySequence had all the methods defined. It however recognizes list, tuple, range, str, bytes, bytearray, array, memoryview and deque, since they are registered as Sequence's virtual subclasses.

Table of required and automatically available special methods:
+------------+------------+------------+------------+--------------+
|            |  Iterable  | Collection |  Sequence  | abc.Sequence |
+------------+------------+------------+------------+--------------+
| iter()     |    REQ     |    REQ     |    Yes     |     Yes      |
| contains() |    Yes     |    Yes     |    Yes     |     Yes      |
| len()      |            |    REQ     |    REQ     |     REQ      |
| getitem()  |            |            |    REQ     |     REQ      |
| reversed() |            |            |    Yes     |     Yes      |
| index()    |            |            |            |     Yes      |
| count()    |            |            |            |     Yes      |
+------------+------------+------------+------------+--------------+
Method iter() is required for 'isinstance(<obj>, abc.Iterable)' to return True, however any object with getitem() will work with any code expecting an iterable.
MutableSequence, Set, MutableSet, Mapping and MutableMapping ABCs are also extendable. Use '<abc>.__abstractmethods__' to get names of required methods.
"""

from collections import abc

class MyAbcSequence(abc.Sequence):
    def __init__(self, a):
        self.a = a
    def __len__(self):
        return len(self.a)
    def __getitem__(self, i):
        return self.a[i]