# Example of try-except block
try:
    # some code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero!")

# Complex Example
try:
    # code that may raise multiple exceptions
    value = int("abc")
except ValueError:
    print("Caught ValueError")
except TypeError:
    print("Caught TypeError")
else:
    print("No exception occurred")
finally:
    print("This always runs")

# Notes:
# - Code inside the 'else' block will only be executed if 'try' block had no exceptions.
# - Code inside the 'finally' block will always be executed (unless a signal is received).
# - All variables that are initialized in executed blocks are also visible in all subsequent blocks, as well as outside the try statement (only function block delimits scope).
# - To catch signals use: signal.signal(signal_number, handler_function)

# Catching Exceptions:
# except ExceptionType:
# except ExceptionType as name:
# except (ExceptionType1, ExceptionType2):
# except (ExceptionType1, ExceptionType2) as name:
# Also catches subclasses of the exception.

# Use traceback.print_exc() to print the full error message to stderr.
# Use print(name) to print just the cause of the exception (its arguments).
# Use logging.exception(str) to log the passed message, followed by the full error message of the caught exception.
# Use sys.exc_info() to get exception type, object, and traceback of caught exception.

# Raising Exceptions:
# raise ExceptionType
# raise ExceptionType()
# raise ExceptionType(obj, ...)
# Re-raising caught exception:
# except ExceptionType as name:
#     ...
#     raise

# Exception Object:
# arguments = name.args
# exc_type  = name.__class__
# filename  = name.__traceback__.tb_frame.f_code.co_filename
# func_name = name.__traceback__.tb_frame.f_code.co_name
# line      = linecache.getline(filename, name.__traceback__.tb_lineno)
# trace_str = ''.join(traceback.format_tb(name.__traceback__))
# error_msg = ''.join(traceback.format_exception(type(name), name, name.__traceback__))

# Built-in Exceptions (partial list):
# BaseException
#  +-- SystemExit                   # Raised by the sys.exit() function.
#  +-- KeyboardInterrupt            # Raised when the user hits the interrupt key (ctrl-c).
#  +-- Exception                    # User-defined exceptions should be derived from this class.
#       +-- ArithmeticError         # Base class for arithmetic errors such as ZeroDivisionError.
#       +-- AssertionError          # Raised by `assert <exp>` if expression returns false value.
#       +-- AttributeError          # Raised when object doesn't have requested attribute/method.
#       +-- EOFError                # Raised by input() when it hits an end-of-file condition.
#       +-- LookupError             # Base class for errors when a collection can't find an item.
#       |    +-- IndexError         # Raised when a sequence index is out of range.
#       |    +-- KeyError           # Raised when a dictionary key or set element is missing.
#       +-- MemoryError             # Out of memory. May be too late to start deleting variables.
#       +-- NameError               # Raised when nonexistent name (variable/func/class) is used.
#       |    +-- UnboundLocalError  # Raised when local name is used before it's being defined.
#       +-- OSError                 # Errors such as FileExistsError/TimeoutError.
#       |    +-- ConnectionError    # Errors such as BrokenPipeError/ConnectionAbortedError.
#       +-- RuntimeError            # Raised by errors that don't fall into other categories.
#       |    +-- NotImplementedError# Can be raised by abstract methods or by unfinished code.
#       |    +-- RecursionError     # Raised if max recursion depth is exceeded (3k by default).
#       +-- StopIteration           # Raised when an empty iterator is passed to next().
#       +-- TypeError               # When an argument of the wrong type is passed to function.
#       +-- ValueError              # When argument has the right type but inappropriate value.

# Collections and their exceptions:
# +-----------+------------+------------+------------+
# |           |    List    |    Set     |    Dict    |
# +-----------+------------+------------+------------+
# | getitem() | IndexError |            |  KeyError  |
# | pop()     | IndexError |  KeyError  |  KeyError  |
# | remove()  | ValueError |  KeyError  |            |
# | index()   | ValueError |            |            |
# +-----------+------------+------------+------------+

# Useful built-in exceptions:
# raise TypeError('Argument is of the wrong type!')
# raise ValueError('Argument has the right type but an inappropriate value!')
# raise RuntimeError('I am too lazy to define my own exception!')

# User-defined Exceptions:
class MyError(Exception):
    pass

class MyInputError(MyError):
    pass