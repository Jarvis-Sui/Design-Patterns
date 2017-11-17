import abc
import copy


class AbstractPrototype(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def clone(self):
        pass


class ConcretePrototype1(AbstractPrototype):
    def __init__(self):
        self.x = self.__class__.__name__ + '.x'

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype2(AbstractPrototype):
    def __init__(self):
        self.x = self.__class__.__name__ + '.x'

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    for cp in [ConcretePrototype1(), ConcretePrototype2()]:
        obj = cp.clone()
        print obj.x