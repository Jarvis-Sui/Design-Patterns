class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.x = self.__class__.__name__ + '.x'


if __name__ == '__main__':
    mc = MyClass()
    mc2 = MyClass()
    assert id(mc) == id(mc2)