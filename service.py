from enum import Enum

class SystemService(object):
    def __init__(self):
        pass

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_state):
        self._status = new_state

    @property
    def isAvailable (self):
        return self._isAvailable

    @isAvailable.setter
    def isAvailable(self, new_state):
        self._isAvailable = new_state

    def run(self):
        self.status = 'on'

    def stop(self):
        self.status = 'off'

    def restart(self):
        self.status = 'off'
        print('restarting')
        self.status = 'on'
