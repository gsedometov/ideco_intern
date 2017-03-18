from aiohttp import web

from service import daemon

async def start(request):
    daemon.run()
    return web.Response(text='Сервис запущен')

async def restart(request):
    daemon.restart()
    return web.Response(text='Сервис перезапущен')

async def stop(request):
    daemon.stop()
    return web.Response(text='Сервис остановлен')

async def switch(request):
    daemon.switch()
    return web.Response(text='Сервис переключён')
