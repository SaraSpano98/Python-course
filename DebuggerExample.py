"""Decorator that prints function's name every time the function is called."""

from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y

# wraps is a helper decorator that copies the metadata of the passed function (func) to the function it is wrapping (out).
# Without it, 'add.__name__' would return 'out'.
