import time

from ..service import SystemService

def test_init():
    test_daemon = SystemService()
    assert test_daemon.check_status() in ('on', 'off')

def test_run():
    test_daemon = SystemService()
    test_daemon.run()
    time.sleep(.5)
    assert test_daemon.status == 'on'

def test_stop():
    test_daemon = SystemService()
    test_daemon.stop()
    time.sleep(.5)
    assert test_daemon.status == 'off'

def test_restart():
    test_daemon = SystemService()
    test_daemon.run()
    time.sleep(.5)
    test_daemon.restart()
    time.sleep(.5)
    test_daemon.status == 'on'
