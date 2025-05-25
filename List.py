my_list = [1, 2, 3]  # Creates a list object. Also list(<collection>).

element = my_list[0]            # First index is 0. Last -1. Allows assignments.
sublist = my_list[1:3]          # Also my_list[from_inclusive : to_exclusive : ±step].

my_list.append(4)               # Appends element to the end. Also my_list += [4].
my_list.extend([5, 6])          # Appends elements to the end. Also my_list += [5, 6].

my_list.sort()                  # Sorts elements in ascending order.
my_list.reverse()               # Reverses the list in-place.
sorted_list = sorted(my_list)   # Returns new list with sorted elements.
reversed_iter = reversed(my_list) # Returns reversed iterator of elements.

max_element = max(my_list)      # Returns largest element. Also min(1, 2, 3).
total = sum(my_list)            # Returns sum of elements. Also math.prod(my_list).

list_a = [1, 2, 3]
list_b = [4, 5, 6]
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
collection = [(1, 2), (3, 1), (2, 3)]
sorted_by_second = sorted(collection, key=lambda el: el[1])
sorted_by_both   = sorted(collection, key=lambda el: (el[1], el[0]))
import itertools
flatter_list     = list(itertools.chain.from_iterable([list_a, list_b]))

# For details about sort(), sorted(), min() and max() see Sortable.
# Module operator has function itemgetter() that can replace listed lambdas.
# This text uses the term collection instead of iterable. For rationale see Collection.

length = len(my_list)           # Returns number of items. Also works on dict, set and string.
count_ones = my_list.count(1)   # Returns number of occurrences of 1 in my_list. Also `if 1 in my_list: ...`.
index_of_two = my_list.index(2) # Returns index of the first occurrence of 2 or raises ValueError.
last_element = my_list.pop()    # Removes and returns item from the end or at index if passed.
my_list.insert(1, 10)           # Inserts 10 at index 1 and moves the rest to the right.
my_list.remove(10)              # Removes first occurrence of 10 or raises ValueError.
my_list.clear()                 # Removes all items. Also works on dictionary and set.