import asyncio
import time
from enum import Enum

class SystemService(object):
    def __init__(self):
        self._status = 'off'

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_state):
        self._status = new_state

    @property
    def isAvailable (self):
        try:
            f = open('is_available')
        except FileNotFoundError:
            self.isAvailable = False
        try:
            state = eval(f.read())
        except ValueError:
            raise ValueError('Файл состояния повреждён')
        return state

    @isAvailable.setter
    def isAvailable(self, new_state):
        with open('is_available', 'w') as f:
            f.write(str(new_state))

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
