# Tuple examples
empty_tuple = ()                               # Empty tuple.
single_element_tuple = (1,)                    # Or: 1,
multi_element_tuple = (1, 2, 3)                # Or: 1, 2, 3
# Tuple is an immutable and hashable list.

# NAMED TUPLE
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(1, y=2)
print(p)
print(p[0], p.x)
(1, 1)