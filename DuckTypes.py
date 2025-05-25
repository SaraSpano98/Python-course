# A duck type is an implicit type that prescribes a set of special methods. Any object that has those methods defined is considered a member of that duck type.

# Comparable
# If eq() method is not overridden, it returns 'id(self) == id(other)', which is the same as 'self is other'. That means all user-defined objects compare not equal by default, because id() returns object's unique identification number (its memory address).
# Only the left side object has eq() method called, unless it returns NotImplemented, in which case the right object is consulted. False is returned if both return NotImplemented.
# Ne() automatically works on any object that has eq() defined.
class MyComparable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    

# Hashable
# Hashable object needs both hash() and eq() methods and its hash value must not change.
# Hashable objects that compare equal must have the same hash value, meaning default hash() that returns 'id(self)' will not do. That is why Python automatically makes classes unhashable if you only implement eq().
class MyHashable:
    def __init__(self, a):
        self._a = a
    @property
    def a(self):
        return self._a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __hash__(self):
        return hash(self.a)
    

# Sortable
# With 'total_ordering' decorator, you only need to provide eq() and one of lt(), gt(), le() or ge() special methods (used by <, >, <=, >=) and the rest will be automatically generated.
# Functions sorted() and min() only require lt() method, while max() only requires gt(). However, it is best to define them all so that confusion doesn't arise in other contexts.
# When two lists, strings or dataclasses are compared, their values get compared in order until a pair of unequal values is found. The comparison of this two values is then returned. The shorter sequence is considered smaller in case of all values being equal.
# To sort collection of strings in proper alphabetical order pass 'key=locale.strxfrm' to sorted() after running 'locale.setlocale(locale.LC_COLLATE, "en_US.UTF-8")'.
from functools import total_ordering

@total_ordering
class MySortable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.a < other.a
        return NotImplemented
    

# Iterator
# Any object that has methods next() and iter() is an iterator.
# Next() should return next item or raise StopIteration exception.
# Iter() should return an iterator of remaining items, i.e. 'self'.
# Any object that has iter() method can be used in a for loop.
class Counter:
    def __init__(self):
        self.i = 0
    def __next__(self):
        self.i += 1
        return self.i
    def __iter__(self):
        return self
# >>> counter = Counter()
# >>> next(counter), next(counter), next(counter)
# (1, 2, 3)
# Python has many different iterator objects:
# Sequence iterators returned by the iter() function, such as list_iterator and set_iterator.
# Objects returned by the itertools module, such as count, repeat and cycle.
# Generators returned by the generator functions and generator expressions.
# File objects returned by the open() function, etc.


# Callable
# All functions and classes have a call() method, hence are callable.
# Use 'callable(<obj>)' or 'isinstance(<obj>, collections.abc.Callable)' to check if object is callable. Calling an uncallable object raises TypeError.
# When this cheatsheet uses '<function>' as an argument, it means '<callable>'.
class Counter:
    def __init__(self):
        self.i = 0
    def __call__(self):
        self.i += 1
        return self.i
# >>> counter = Counter()
# >>> counter(), counter(), counter()
# (1, 2, 3)


# Context Manager
# With statements only work on objects that have enter() and exit() special methods.
# Enter() should lock the resources and optionally return an object.
# Exit() should release the resources (for example close a file).
# Any exception that happens inside the with block is passed to the exit() method.
# The exit() method can suppress the exception by returning a true value.
class MyOpen:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    def __exit__(self, exc_type, exception, traceback):
        self.file.close()
# >>> with open('test.txt', 'w') as file:
# ...     file.write('Hello World!')
# >>> with MyOpen('test.txt') as file:
# ...     print(file.read())
# Hello World!