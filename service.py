from enum import Enum

class SystemService(object):
    def __init__(self):
        self._status = 'off'
        self._isAvailable = True

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
        print('starting')
        self.status = 'on'

    def stop(self):
        print('stopping')
        self.status = 'off'

    def restart(self):
        self.status = 'off'
        print('restarting')
        self.status = 'on'

    def switch(self):
        self.isAvailable = not self.isAvailable

daemon = SystemService()
