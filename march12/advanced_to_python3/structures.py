class Structure:

    _fields = []

    def __init__(self, *args):
        for name, val in zip(self._fields, *args):
            setattr(self, name, val)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    # def __init__(self, name, shares, price):
    #     self.name = name
    #     self.shares = shares
    #     self.price = price


class Point:

    _fields = ['x', 'y']
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y


class Address:

    _fields = ['hostname', 'port']
    #
    # def __init__(self, hostname, port):
    #     self.hostname = hostname
    #     self.port = port



