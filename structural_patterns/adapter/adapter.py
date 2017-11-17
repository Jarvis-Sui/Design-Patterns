import abc


class Target(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._adaptee = Adaptee()


class Adapter(Target):
    def request(self, client_param):
        adapted_param = self._adapt(client_param)
        self._adaptee.specific_request(adapted_param)

    def _adapt(self, param):
        return 'adapt ' + param


class Adaptee(object):
    def specific_request(self, param):
        print self.__class__.__name__, param


if __name__ == '__main__':
    adapt = Adapter()
    adapt.request('my param')

