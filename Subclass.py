# Inheritance is a mechanism that enables a class to extend another class (subclass to extend its parent), and by doing so inherit all its methods and attributes.
# Subclass can then add its own methods and attributes or override inherited ones by reusing their names.

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Person({self.name!r})'
    def __lt__(self, other):
        return self.name < other.name

class Employee(Person):
    def __init__(self, name, staff_num):
        super().__init__(name)
        self.staff_num = staff_num
    def __repr__(self):
        return f'Employee({self.name!r}, {self.staff_num})'

# Example usage:
people = {Person('Ann'), Employee('Bob', 0)}
sorted_people = sorted(people)
print(sorted_people)  # [Person('Ann'), Employee('Bob', 0)]

# Type Annotations
# They add type hints to variables, arguments and functions ('def f() -> <type>:').
# Hints are used by type checkers like mypy, data validation libraries such as Pydantic and lately also by Cython compiler. However, they are not enforced by CPython interpreter.
from collections import abc

# <name>: <type> [| ...] [= <obj>]
# <name>: list/set/abc.Iterable/abc.Sequence[<type>] [= <obj>]
# <name>: dict/tuple[<type>, ...] [= <obj>]