# Example of using Enum in Python

from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = 3
    YELLOW = (4, "yellow")  # Tuple as value

# Accessing members
c = Color.RED
print(c.name)    # 'RED'
print(c.value)   # 1

# List all members
print(list(Color))

# Get member by name
print(Color['GREEN'])

# Get member by value
print(Color(3))

# Get all member names and values
print([a.name for a in Color])
print([a.value for a in Color])