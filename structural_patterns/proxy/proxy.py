import abc


class Subject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do(self):
        pass


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def do(self):
        print 'call from', self.__class__.__name__
        self._real_subject.do()


class RealSubject(Subject):
    def do(self):
        print 'do sth'


if __name__ == '__main__':
    # when a RealSubject is needed, create one and wrap it with Proxy
    rs = RealSubject()
    proxy = Proxy(rs)
    proxy.do()