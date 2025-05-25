# Each abstract base class specifies a set of virtual subclasses.
# These classes are then recognized by isinstance() and issubclass() as subclasses of the ABC, although they are really not.
# ABC can also manually decide whether or not a specific class is its virtual subclass, usually based on which methods the class has implemented.
# For instance, Iterable ABC looks for method __iter__(), while Collection ABC looks for __iter__(), __contains__() and __len__().

from collections.abc import Iterable, Collection, Sequence

print(isinstance([1, 2, 3], Iterable))  # True

# Examples:
# list, range, str: Iterable, Collection, Sequence
# dict, set: Iterable, Collection
# iter: Iterable

from numbers import Number, Complex, Real, Rational, Integral

print(isinstance(123, Number))  # True

# Examples:
# int: Number, Complex, Real, Rational, Integral
# fractions.Fraction: Number, Complex, Real, Rational
# float: Number, Complex, Real
# complex: Number, Complex
# decimal.Decimal: Number