# If variable is being assigned to anywhere in the scope, it is regarded as a local variable, unless it is declared as a 'global' or a 'nonlocal'.

def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out

# Example usage:
counter = get_counter()
print(counter(), counter(), counter())  # Output: (1, 2, 3)

# Decorator
# A decorator takes a function, adds some functionality and returns it.
# It can be any callable, but is usually implemented as a function that returns a closure.

# Example decorator usage:
# @decorator_name

def function_that_gets_passed_to_decorator():
    pass
   