"""
Decorator that uses class variables to generate __init__(), __repr__(), and __eq__() special methods.

Objects can be made sortable with 'order=True' and immutable with 'frozen=True'.
For an object to be hashable, all attributes must be hashable and 'frozen' must be True.
Function field() is needed because '<attr_name>: list = []' would make a list that is shared among all instances. Its 'default_factory' argument can be any callable.
For attributes of arbitrary type use 'typing.Any'.
"""

from dataclasses import dataclass, field, make_dataclass
from typing import Any, List

@dataclass(order=False, frozen=False)
class Example:
    x: int
    y: float = 0.0
    tags: List[Any] = field(default_factory=list)

# Example usages of make_dataclass:
P1 = make_dataclass('P1', ['x', 'y'])
P2 = make_dataclass('P2', [('x', float), ('y', float)])
P3 = make_dataclass('P3', [('x', float, 0), ('y', float, 0)])