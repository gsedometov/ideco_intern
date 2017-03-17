from aiohttp import web

from service import daemon

def start(request):
    daemon.run()
    return web.Response(text='Сервис запущен')

def restart(request):
    daemon.restart()
    return web.Response(text='Сервис перезапущен')

def stop(request):
    daemon.stop()
    return web.Response(text='Сервис остановлен')

def switch(request):
    daemon.switch()
    return web.Response(text='Сервис переключён')
