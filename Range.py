# Immutable and hashable sequence of integers.

# range(stop)                      # I.e. range(to_exclusive).
# range(start, stop)               # I.e. range(from_inclusive, to_exclusive).
# range(start, stop, step)         # I.e. range(from_inclusive, to_exclusive, ±step).

# Example usage:
print([i for i in range(3)])  # Output: [0, 1, 2]



#ENUMERATE
class Range:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("Range expected at most 3 arguments, got {}".format(len(args)))

    def __iter__(self):
        current = self.start
        while (self.step > 0 and current < self.stop) or (self.step < 0 and current > self.stop):
            yield current
            current += self.step

    def __repr__(self):
        return "Range({}, {}, {})".format(self.start, self.stop, self.step)
    
# for i, el in enumerate([10, 20, 30], start=0):   # Returns next element and its index on each pass.
#print(i, el) 


