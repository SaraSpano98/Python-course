# Lambda
# func = lambda: return_value                     # A single statement function.
# func = lambda arg_1, arg_2: return_value       # Also allows default arguments.

# Comprehensions
example_list = [i+1 for i in range(10)]                   # Or: [1, 2, ..., 10]
example_iter = (i for i in range(10) if i > 5)            # Or: iter([6, 7, 8, 9])
example_set  = {i+5 for i in range(10)}                   # Or: {5, 6, ..., 14}
example_dict = {i: i*2 for i in range(10)}                # Or: {0: 0, 1: 2, ..., 9: 18}
# [l+r for l in 'abc' for r in 'abc']             # Inner loop is on the right side.
# ['aa', 'ab', 'ac', ..., 'cc']

# Map, Filter, Reduce
from functools import reduce
example_map = map(lambda x: x + 1, range(10))            # Or: iter([1, 2, ..., 10])
example_filter = filter(lambda x: x > 5, range(10))      # Or: iter([6, 7, 8, 9])
example_reduce = reduce(lambda out, x: out + x, range(10))  # Or: 45

# Any, All
# bool_any = any(collection)                          # Is `bool(el)` True for any el?
# bool_all = all(collection)                          # True for all? Also True if empty.

# Conditional Expression
# obj = exp if condition else exp             # Only one expression is evaluated.
example_conditional = [i if i else 'zero' for i in (0, 1, 2, 3)]      # `any([0, '', [], None]) == False`
# ['zero', 1, 2, 3]

# And, Or
# obj = exp and exp [and ...]                   # Returns first false or last operand.
# obj = exp or exp [or ...]                     # Returns first true or last operand.

# Walrus Operator
example_walrus = [i for a in '0123' if (i := int(a)) > 0]        # Assigns to variable mid-sentence.
# [1, 2, 3]

# Named Tuple, Enum, Dataclass
from collections import namedtuple
Point = namedtuple('Point', 'x y')                  # Creates tuple's subclass.
point = Point(0, 0)                                 # Returns its instance.

from enum import Enum
Direction = Enum('Direction', 'N E S W')            # Creates Enum's subclass.
direction = Direction.N                             # Returns its member.

from dataclasses import make_dataclass
Player = make_dataclass('Player', ['loc', 'dir'])   # Creates a class.
player = Player(point, direction)                   # Returns its instance.