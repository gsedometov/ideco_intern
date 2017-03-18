import subprocess

class SystemService(object):
    '''
    Класс, реализующий взаимодействие с системной службой
    Свойства:
    isAvailable - активность сервиса в (связана с чекбоксом)
    status (read-only) - статус сервиса ('on'/'off')
    Методы:
    run, stop, restart, switch
    '''
    def __init__(self):
        pass

    def check_status(self):
        reader = subprocess.Popen(['sudo', 'systemctl', 'status', 'dummy'], stdout=subprocess.PIPE)
        #Skip first 2 lines
        for _ in range(2):
            reader.stdout.readline()
        current_status = reader.stdout.readline().split()[1]
        if current_status in (b'active', b'activating'):
            status = 'on'
        else:
            status = 'off'
        return status

    @property
    def status(self):
        return self.check_status()

    @property
    def isAvailable(self):
        try:
            f = open('is_available')
        except FileNotFoundError:
            self.isAvailable = False
            return self.isAvailable()
        try:
            state = eval(f.read())
        except:
            raise ValueError('Файл состояния повреждён')
        return state

    @isAvailable.setter
    def isAvailable(self, new_state):
        with open('is_available', 'w') as f:
            f.write(str(new_state))

    def run(self):
        if self.check_status() == 'on':
            print('service already started')
            return
        print('starting')
        subprocess.Popen('sudo systemctl start dummy'.split())

    def stop(self):
        if self.check_status() == 'off':
            print('service already stopped')
            return
        print('stopping')
        subprocess.Popen('sudo systemctl stop dummy'.split())

    def restart(self):
        if self.check_status() == 'off':
            print('service is not started')
            return
        print('restarting')
        subprocess.Popen('sudo systemctl restart dummy'.split())

    def switch(self):
        self.isAvailable = not self.isAvailable

daemon = SystemService()
