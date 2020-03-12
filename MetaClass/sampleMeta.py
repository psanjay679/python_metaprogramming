from Debugly.debugly import debugmethods


class MyType(type):

    def __new__(cls, name, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("No")

        clsobj = super(MyType, cls).__new__(cls, name, bases, clsdict)
        return clsobj


class debugMeta(type):
    def __new__(cls, *args, **kwargs):
        clsobj = super().__new__(cls, *args, **kwargs)

        clsobj = debugmethods(clsobj)
        return clsobj


class Span(metaclass=debugMeta):
    def __init__(self):
        super(Span, self).__init__()

        pass


class A(Span):
    def __init__(self):
        super(A, self).__init__()

        pass


class B(Span):
    def __init__(self):
        super(B, self).__init__()

        pass


class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        pass


c = C()