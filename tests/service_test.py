import time

from ..service import SystemService

def test_init():
    test_daemon = SystemService()
    #enabled = test_daemon.isAvailable
    #assert enabled == False
    assert test_daemon.status == 'off'

def test_run():
    test_daemon = SystemService()
    test_daemon.run()
    assert test_daemon.status == 'on'

def test_stop():
    test_daemon = SystemService()
    test_daemon.stop()
    assert test_daemon.status == 'off'

def test_restart():
    test_daemon = SystemService()
    test_daemon.run()
    test_daemon.restart()
    test_daemon.status == 'on'
