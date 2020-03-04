class Structure:
    _fields = []

    def __init__(self, *args):
        for key, value in zip(self._fields, args):
            setattr(self, key, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


class Host(Structure):
    _fields = ['address', 'port']


s = Stock(1, 2, 3)
print(s.name)
print(s.shares)
print(s.price)