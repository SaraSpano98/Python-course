# Example of a closure in Python

def get_multiplier(a):
    def out(b):
        return a * b
    return out

multiply_by_3 = get_multiplier(3)
result = multiply_by_3(10)
print(result)  # Output: 30

# Any value that is referenced from within multiple nested functions gets shared.