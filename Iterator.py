# Potentially endless stream of elements.

collection = [1, 2, 3, 4]
iterator = iter(collection)                # `iter(iterator)` returns unmodified iterator.

def func():
	for i in range(5):
		yield i
function_iterator = iter(func())           # Example of creating an iterator from a generator function

element = next(iterator, None)             # Raises StopIteration or returns 'None' on end.
remaining_elements = list(iterator)        # Returns a list of iterator's remaining elements.