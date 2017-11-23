class Data(object):
    def __init__(self, attr1, attr2):
        self._attr1 = attr1
        self._attr2 = attr2

    @property
    def attr1(self):
        return self._attr1

    @property
    def attr2(self):
        return self._attr2


class Target(object):
    def __init__(self, attr1, attr2):
        self._data = Data(attr1, attr2)

    def do(self):
        print 'result is', self._data.attr1 + self._data.attr2


if __name__ == '__main__':
    tar = Target('a', 'b')
    tar.do()