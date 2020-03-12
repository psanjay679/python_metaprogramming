from Debugly.debugly import debugmethods


@debugmethods
class Spam:

    def a(self):
        pass

    def b(self):
        pass


S = Spam()
S.a()