# <bool>   = <D/T/DTn> > <D/T/DTn>            # Ignores time jumps (fold attribute). Also ==.
# <bool>   = <DTa>     > <DTa>                # Ignores time jumps if they share tzinfo object.
# <TD>     = <D/DTn>   - <D/DTn>              # Ignores jumps. Convert to UTC for actual delta.
# <TD>     = <DTa>     - <DTa>                # Ignores jumps if they share tzinfo object.
# <D/DT>   = <D/DT>    ± <TD>                 # Returned datetime can fall into missing hour.
# <TD>     = <TD>      * <float>              # Also `<TD> = abs(<TD>)`, `<TD> = <TD> ± <TD>`.
# <float>  = <TD>      / <TD>                 # Also `(<int>, <TD>) = divmod(<TD>, <TD>)`.


# Function
# Independent block of code that returns a value when called.

# def <func_name>(<nondefault_args>): ...                  # E.g. `def func(x, y): ...`.
# def <func_name>(<default_args>): ...                     # E.g. `def func(x=0, y=0): ...`.
# def <func_name>(<nondefault_args>, <default_args>): ...  # E.g. `def func(x, y=0): ...`.
# Function returns None if it doesn't encounter 'return <obj/exp>' statement.
# Run 'global <var_name>' inside the function before assigning to global variable.
# Default values are evaluated when function is first encountered in the scope. 
# Any mutation of a mutable default value will persist between invocations!


# Function Call
# <obj> = <function>(<positional_args>)                    # E.g. `func(0, 0)`.
# <obj> = <function>(<keyword_args>)                       # E.g. `func(x=0, y=0)`.
# <obj> = <function>(<positional_args>, <keyword_args>)    # E.g. `func(0, y=0)`.


# Splat Operator
# Splat expands a collection into positional arguments, while splatty-splat expands a dictionary into keyword arguments.

args, kwargs = (1, 2), {'z': 3}
def func(x, y, z):
    return x + y + z
func(*args, **kwargs)
# Is the same as:
func(1, 2, z=3)


# Inside Function Definition
# Splat combines zero or more positional arguments into a tuple, while splatty-splat 
# combines zero or more keyword arguments into a dictionary.

def add(*a):
    return sum(a)
print(add(1, 2, 3))


# Allowed compositions of arguments and the ways they can be called:
# +---------------------------+--------------+--------------+----------------+
# |                           |  func(1, 2)  | func(1, y=2) | func(x=1, y=2) |
# +---------------------------+--------------+--------------+----------------+
# | func(x, *args, **kwargs): |     yes      |     yes      |      yes       |
# | func(*args, y, **kwargs): |              |     yes      |      yes       |
# | func(*, x, **kwargs):     |              |              |      yes       |
# +---------------------------+--------------+--------------+----------------+


# Other Uses
# <list>  = [*<collection> [, ...]]  # Or: list(<coll>) [+ ...]
# <tuple> = (*<collection>, [...])   # Or: tuple(<coll>) [+ ...]
# <set>   = {*<collection> [, ...]}  # Or: set(<coll>) [| ...]
# <dict>  = {**<dict> [, ...]}       # Or: <dict> | ...

# head, *body, tail = <collection>   # Head or tail can be omitted.