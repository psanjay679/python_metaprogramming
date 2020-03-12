def debugattr(cls):

    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):

        print("Get:", name)

        return orig_getattribute(self, name)

    cls.__getattribute__ = __getattribute__

    return cls


class debugMeta(type):

    # def __init__(self):

    def __new__(cls, *args, **kwargs):
        clsobj = super().__new__(cls, *args, **kwargs)

        clsobj = debugattr(clsobj)
        return clsobj


class MyType(type):
    def __new__(cls, clsname, base, clsdict):
        if len(base) > 1:
            raise TypeError("NO")

        return super().__new__(cls, clsname, base, clsdict)


class Spam(metaclass=debugMeta):

    def __init__(self):
        self.x = 10
        self.y = 20


a = Spam()

print(a.x)
print(a.y)


class Base(metaclass=MyType):
    pass


class A(Base):
    pass


class B(Base):
    pass

class C(A, B):
    pass

A()
B()
C()
