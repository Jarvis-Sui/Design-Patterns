import abc


class FlyWeight(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def operate(self):
        pass


class ConcreteFlyWeight(FlyWeight):
    def __init__(self, instrinsic_state):
        self._instrinsic_state = instrinsic_state

    def set_extrinsic(self, extrinsic_state):
        self._extrinsic_state = extrinsic_state

    def operate(self):
        print 'operate on', self._instrinsic_state, self._extrinsic_state


class Factory(object):
    def __init__(self):
        self._flyweights = {}

    def get_flyweights(self, instrinsic):
        if instrinsic in self._flyweights:
            return self._flyweights[instrinsic]
        else:
            print 'create a flyweight with instrinsic:', instrinsic
            flyweight = ConcreteFlyWeight(instrinsic)
            self._flyweights[instrinsic] = flyweight
            return flyweight


if __name__ == '__main__':
    import random
    instrinsic_state = ['is_1', 'is_2', 'is_3']
    factory = Factory()
    for i in range(5):
        ins = random.choice(instrinsic_state)
        flyweight = factory.get_flyweights(ins)
        flyweight.set_extrinsic('ext_%d' % i)
        flyweight.operate()


