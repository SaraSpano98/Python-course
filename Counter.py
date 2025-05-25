#COUNTER
from collections import Counter
counter = Counter(['blue', 'blue', 'blue', 'red', 'red'])
counter['yellow'] += 1
print(counter.most_common())
[('blue', 3), ('red', 2), ('yellow', 1)] 