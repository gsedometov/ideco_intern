from aiohttp import web
from jinja2.loaders import FileSystemLoader
import aiohttp_jinja2

from service import daemon
from view import index

def start(request):
    daemon.run()
    return web.Response(text='Сервис запущен')

def restart(request):
    daemon.restart()
    return web.Response(text='Сервис перезапущен')

def stop(request):
    daemon.stop()
    return web.Response(text='Сервис остановлен')

def main():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=FileSystemLoader(''))
    app.router.add_static('/static', 'static')
    app.router.add_get('/', index)
    app.router.add_get('/start', start)
    app.router.add_get('/restart', restart)
    app.router.add_get('/stop', stop)
    web.run_app(app)


if __name__ == '__main__':
    main()
