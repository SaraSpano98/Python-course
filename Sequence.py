# Only required methods are __getitem__() and __len__().
# __getitem__() should return an item at the passed index or raise IndexError.
# __iter__() and __contains__() automatically work on any object that has __getitem__() defined.
# __reversed__() automatically works on any object that has __getitem__() and __len__() defined. It returns reversed iterator of object's items.

class MySequence:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
    def __len__(self):
        return len(self.a)
    def __getitem__(self, i):
        return self.a[i]
    def __reversed__(self):
        return reversed(self.a)

# Discrepancies between glossary definitions and abstract base classes:
# Python's glossary defines iterable as any object with special methods __iter__() and/or __getitem__() and sequence as any object with __getitem__() and __len__(). It doesn't define collection.
# Passing ABC Iterable to isinstance() or issubclass() only checks whether object/class has special method __iter__(), while ABC Collection checks for __iter__(), __contains__() and __len__().