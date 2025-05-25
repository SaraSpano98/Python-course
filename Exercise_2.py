def bar():
    print("#" + 16 * "=" + "#")


def top():
    for line in range(1, 5):
        spaces = (-2 * line + 8) * " "
        dots = (4 * line - 4) * "."
        print(
            "|" + spaces + "<>" + dots + "<>" + spaces + "|"
        )


def bottom():
    for line in range(4, 0, -1):
        spaces = (-2 * line + 8) * " "
        dots = (4 * line - 4) * "."
        print(
            "|" + spaces + "<>" + dots + "<>" + spaces + "|"
        )
