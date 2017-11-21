import abc


class Component(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def operate(self):
        pass


class Decorator(Component):
    __metaclass__ = abc.ABCMeta

    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operate(self):
        pass


class ConcreteDecorator1(Decorator):
    def operate(self):
        print 'add operation', self.__class__.__name__
        self._component.operate()


class ConcreteDecorator2(Decorator):
    def operate(self):
        print 'add operation', self.__class__.__name__
        self._component.operate()


class ConcreteComponent(Component):
    def operate(self):
        print 'operate', self.__class__.__name__

if __name__ == '__main__':
    comp = ConcreteComponent()
    comp.operate()
    print '=' * 10
    comp1 = ConcreteDecorator1(comp)
    comp1.operate()
    print '=' * 10
    comp2 = ConcreteDecorator2(comp1)
    comp2.operate()