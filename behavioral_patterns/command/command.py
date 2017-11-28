import abc


class Light(object):
    # Reciever
    def turnon(self):
        print 'turnon the light'

    def turnoff(self):
        print 'turnoff the light'


class Switch(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        self._history = ()

    def history(self):
        return self._history

    def execute(self, command):
        self._history = self._history + (command,)
        command.execute()


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, receiver):
        self._receiver = receiver
    
    @abc.abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def execute(self):
        self._receiver.turnon()


class TurnOffCommand(Command):
    def execute(self):
        self._receiver.turnoff()


class LightSwitchClient(object):
    def __init__(self):
        self._switch = Switch()
        self._light = Light()

    def press(self, cmd):
        cmd = cmd.strip().upper()
        if cmd == 'ON':
            self._switch.execute(TurnOnCommand(self._light))
        elif cmd == 'OFF':
            self._switch.execute(TurnOffCommand(self._light))


if __name__ == '__main__':
    lsc = LightSwitchClient()
    lsc.press("ON")
    lsc.press("OFF")
