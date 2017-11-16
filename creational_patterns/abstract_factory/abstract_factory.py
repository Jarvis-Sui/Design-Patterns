import abc


class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        print self.__class__.__name__, 'creates a product A'
        return ConcreteProductA()

    def create_product_b(self):
        print self.__class__.__name__, 'creates a product B'
        return ConcreteProductB()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        print self.__class__.__name__, 'creates a product A2'
        return ConcreteProductA2()

    def create_product_b(self):
        print self.__class__.__name__, 'creates a product B2'
        return ConcreteProductB2()


class AbstractProductA(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def interface_a(self):
        pass


class AbstractProductB(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductA(AbstractProductA):
    def interface_a(self):
        print self.__class__.__name__, 'calls interface A'


class ConcreteProductA2(AbstractProductA):
    def interface_a(self):
        print self.__class__.__name__, 'calls interface A'


class ConcreteProductB(AbstractProductB):
    def interface_b(self):
        print self.__class__.__name__, 'calls interface B'


class ConcreteProductB2(AbstractProductB):
    def interface_b(self):
        print self.__class__.__name__, 'calls interface B'


if __name__ == '__main__':
    for factory in [ConcreteFactory1(), ConcreteFactory2()]:
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()
