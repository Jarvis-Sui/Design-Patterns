class SubSystem1(object):
    def do(self):
        print self.__class__.__name__, 'do sth'


class SubSystem2(object):
    def do(self):
        print self.__class__.__name__, 'do sth'


class Facade(object):
    def __init__(self):
        self._ss1 = SubSystem1()
        self._ss2 = SubSystem2()

    def do(self):
        self._ss1.do()
        self._ss2.do()


if __name__ == '__main__':
    f = Facade()
    f.do()
