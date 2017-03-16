import aiohttp_jinja2
import aiohttp.web_urldispatcher as dispatcher

from service import daemon

@aiohttp_jinja2.template('index.html')
def index(request):
    resp = {
        'status': daemon.status,
        'availability': daemon.isAvailable,
    }
    return resp
