from functools import partial

# Example usage of functools.partial
def multiply(a, b):
	return a * b

multiply_by_3 = partial(multiply, 3)
result = multiply_by_3(10)
print(result)  # Output: 30

# Partial is also useful in cases when a function needs to be passed as an argument
# because it enables us to set its arguments beforehand.
# A few examples being: defaultdict(func), iter(func, to_exc), and dataclass's field(default_factory=func).