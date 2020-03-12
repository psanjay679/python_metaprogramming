from functools import wraps
from functools import partial


def debug(func=None, *, prefix=""):

    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(msg)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))

    return cls


@debugmethods
class A:
    def __init__(self):
        pass


    @debug(prefix="***")
    def b(self):
        pass

A()

A().b()