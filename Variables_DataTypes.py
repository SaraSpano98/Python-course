x = 5 # x is a variable that holds an integer value
x = "Hello" # x is now a variable that holds a string value

# Numbers on python
intero = 5
virgola_mobile = 5.5

# Strings on python
single_string = 'Hello'
double_string = "Hello"
triple_string = """Hello World"""

# Boolean on python
true_variable = True
false_variable = False


#TYPE

# Everything is an object.
# Every object has a type.
# Type and class are synonymous.

# Example usage:
# my_type = type(my_element)                          # Or: my_element.__class__
# is_str = isinstance(my_element, str)                # Or: issubclass(type(my_element), str)

# Example:
print(type('a'), 'a'.__class__, str)
# Output: (<class 'str'>, <class 'str'>, <class 'str'>)

# Some types do not have built-in names, so they must be imported:
from types import FunctionType, MethodType, LambdaType, GeneratorType, ModuleType