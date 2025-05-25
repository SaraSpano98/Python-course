# Only required method is __iter__(). It should return an iterator of object's items.
# __contains__() automatically works on any object that has __iter__() defined.

class MyIterable:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a

# Example usage:
obj = MyIterable([1, 2, 3])
print([el for el in obj])  # [1, 2, 3]
print(1 in obj)           # True