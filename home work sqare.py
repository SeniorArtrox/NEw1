def print_square(n):
    if n == 1:
        print("*")
    elif n == 2:
        print("*" * 4)
    else:
        print("* " * n)
        spaces = n + 2
        print_square_sp(n, spaces)
        print("* " * n)


def print_square_sp(n, spaces):
    if n == 1:
        print("*" + " " * spaces + "*")
    else:
        print("*" + " " * spaces + "*")
        print_square_sp(n - 1, spaces)


print_square(5)
