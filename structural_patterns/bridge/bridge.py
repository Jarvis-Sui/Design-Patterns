import abc


class Abstractor(object):
    def __init__(self, impl):
        self._impl = impl

    def do(self):
        self._impl.do()


class Implementor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do(self):
        pass


class Implementor1(Implementor):
    def do(self):
        print self.__class__.__name__, 'do sth'


class Implementor2(Implementor):
    def do(self):
        print self.__class__.__name__, 'do sth'


if __name__ == '__main__':
    for impl in [Implementor1(), Implementor2()]:
        a = Abstractor(impl)
        a.do()