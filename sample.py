from debugly import debug
from Debuggableclass import Spam


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
    S = Spam()
    S.a()
