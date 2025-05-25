import itertools as it 

counter = it.count(start=0, step=1)                # Returns updated value endlessly. Accepts floats.
repeater = it.repeat('A', 3)                       # Returns element endlessly or 'times' times.
cycler = it.cycle([1, 2, 3])                       # Repeats the sequence endlessly.

chained = it.chain([1, 2], [3, 4])                 # Empties collections in order (figuratively).
chained_from_iterable = it.chain.from_iterable([[1, 2], [3, 4]])  # Empties collections inside a collection in order.

sliced = it.islice([10, 20, 30, 40], 2)            # Only returns first 'to_exclusive' elements.
sliced_with_step = it.islice([10, 20, 30, 40], 1, 4, 2)  # `to_exclusive, +step_size`. Indices can be None.
                   
