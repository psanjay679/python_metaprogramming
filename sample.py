from debugly import debug


@debug
def add(a, b):
    return a + b


@debug(prefix="@@@")
def sub(a, b):
    return a - b


@debug
def mul(a, b):
    return a * b


@debug
def div(a, b):
    return a / b


if __name__ == '__main__':
    add(2, 3)
    sub(2, 3)
