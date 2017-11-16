import abc


class Product(object):
    def __init__(self, a='a', b='b'):
        self._a = a
        self._b = b

    def __str__(self):
        return "product with a: {0}, b: {1}".format(self._a, self._b)


class AbstractBuilder(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._product = Product()

    @abc.abstractmethod
    def build_part_a(self, value):
        pass

    @abc.abstractmethod
    def build_part_b(self, value):
        pass

    def get_product(self):
        return self._product


class ConcreteBuilder1(AbstractBuilder):
    def build_part_a(self, value='a1'):
        print self.__class__.__name__, 'building part a using', value
        self._product._a = value

    def build_part_b(self, value='b1'):
        print self.__class__.__name__, 'building part b using', value
        self._product._b = value


class ConcreteBuilder2(AbstractBuilder):
    def build_part_a(self, value='a2'):
        print self.__class__.__name__, 'building part a using', value
        self._product._a = value

    def build_part_b(self, value='b2'):
        print self.__class__.__name__, 'building part b using', value
        self._product._b = value


class Director(object):
    @staticmethod
    def construct(builder):
        builder.build_part_a()
        builder.build_part_b()
        return builder.get_product()


if __name__ == '__main__':
    builder1 = ConcreteBuilder1()
    builder2 = ConcreteBuilder2()
    product1 = Director.construct(builder1)
    product2 = Director.construct(builder2)
    print 'builder1 build', product1
    print 'builder2 build', product2