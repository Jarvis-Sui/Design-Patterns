import abc


class Component(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        pass


class Composite(Component):
    def __init__(self):
        self._children = set()

    def add(self, component):
        self._children.add(component)

    def draw(self):
        for comp in self._children:
            comp.draw()


class Circle(Component):
    def draw(self):
        print 'draw', self.__class__.__name__


class Triangle(Component):
    def draw(self):
        print 'draw', self.__class__.__name__


if __name__ == '__main__':
    g = Composite()
    g.add(Circle())
    g.add(Triangle())
    g.draw()