def getTop():
    return "  ______\n /      \\\n/        \\"


def getBottom():
    return "\\        /\n \\______/"


def getLine():
    return "+--------+"


def getStop():
    return "|  STOP  |"


# MAIN

# 1. PRIMA PARTE
print(getTop())
print(getBottom())

# 2. SECONDA PARTE
print("\n" + getBottom())
print(getLine())

# 3. TERZA PARTE
print("\n" + getTop())
print(getStop())
print(getBottom())

# 4. QUARTA PARTE
print("\n" + getTop())
print(getLine())
