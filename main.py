from aiohttp import web

from service import SystemService

async def handle(request):
    global daemon
    #name = request.match_info.get('name', "Anonymous")
    #text = "Hello, " + name
    return web.Response(text=daemon.status)

def main():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)
    web.run_app(app)

if __name__ == '__main__':
    daemon = SystemService()
    daemon.run()
    main()
