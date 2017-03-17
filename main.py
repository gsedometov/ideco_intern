from aiohttp import web
from jinja2.loaders import FileSystemLoader
import aiohttp_jinja2

from service import daemon
from routes import start, restart, stop, switch
from view import index

def main():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=FileSystemLoader(''))
    app.router.add_static('/static', 'static')
    app.router.add_get('/', index)
    app.router.add_get('/start', start)
    app.router.add_get('/restart', restart)
    app.router.add_get('/stop', stop)
    app.router.add_get('/switch', switch)
    web.run_app(app)


if __name__ == '__main__':
    main()
