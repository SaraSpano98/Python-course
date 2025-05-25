# Only required methods are iter() and len(). Len() should return the number of items.
# This cheatsheet actually means '<iterable>' when it uses '<collection>'.
# I chose not to use the name 'iterable' because it sounds scarier and more vague than 'collection'. The main drawback of this decision is that the reader could think a certain function doesn't accept iterators when it does, since iterators are the only built-in objects that are iterable but are not collections.
class MyCollection:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
    def __len__(self):
        return len(self.a)