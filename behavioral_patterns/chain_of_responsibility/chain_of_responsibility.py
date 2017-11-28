import abc


class Handler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self):
        pass


class Handler1(Handler):
    def handle_request(self):
        if True: # can handle it
            print 'request is handled by', self.__class__.__name__
        elif self._successor is not None:
            print 'passing request to successor of', self.__class__.__name__
            self._successor.handle_request()


class Handler2(Handler):
    def handle_request(self):
        if False: # can handle it
            print 'request is handled by', self.__class__.__name__
        elif self._successor is not None:
            print 'passing request to successor of', self.__class__.__name__
            self._successor.handle_request()


if __name__ == '__main__':
    h1 = Handler1()
    h2 = Handler2(h1)
    h2.handle_request()