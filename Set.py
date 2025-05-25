#SET
my_set = {1, 2, 3}                   # Use `set()` for empty set.

my_set.add(4)                                   # Or: my_set |= {4}
my_set.update([5, 6])                           # Or: my_set |= {5, 6}

# Set operations examples
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a.union(set_b)                   # Or: set_a | set_b
intersection_set = set_a.intersection(set_b)     # Or: set_a & set_b
difference_set = set_a.difference(set_b)         # Or: set_a - set_b
sym_diff_set = set_a.symmetric_difference(set_b) # Or: set_a ^ set_b
is_subset = set_a.issubset(set_b)                # Or: set_a <= set_b
is_superset = set_a.issuperset(set_b)            # Or: set_a >= set_b

element = set_a.pop()                            # Raises KeyError if empty.
set_a.remove(2)                                  # Raises KeyError if missing.
set_a.discard(10)                                # Doesn't raise an error.

# FROZEN SET
frozen = frozenset([1, 2, 3]) # is immutable, can be used as a key in a dictionary or an element of a set.