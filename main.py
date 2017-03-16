from aiohttp import web
from jinja2.loaders import FileSystemLoader
import aiohttp_jinja2

from service import daemon
from view import index

def main():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=FileSystemLoader(''))
    app.router.add_get('/', index)
    web.run_app(app)


if __name__ == '__main__':
    main()
