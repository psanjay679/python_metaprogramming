

class MyType(type):
    def __new__(cls, name, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("No")

        clsobj = super(MyType, cls).__new__(cls, name, bases, clsdict)
        return clsobj


class Span(metaclass=MyType):
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

