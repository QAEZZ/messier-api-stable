import aiohttp_jinja2
import jinja2
from aiohttp_jinja2 import *
from aiohttp import web


async def handle_404(request):
    return aiohttp_jinja2.render_template("./static/html/errors/404.html",
                                          request, {})


async def handle_500(request):
    return aiohttp_jinja2.render_template("./static/html/errors/500.html",
                                          request, {})


# shoutout to stack overflow


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        # this is needed to handle ``return web.HTTPNotFound()`` case
        if response.status == 404:
            return web.FileResponse("./static/html/errors/404.html")
        return response
    except web.HTTPException as ex:
        # this is needed to handle ``raise web.HTTPNotFound()`` case
        if ex.status == 404:
            return web.FileResponse("./static/html/errors/404.html")
        raise
    # this is needed to handle non-HTTPException
    except Exception:
        return web.FileResponse("./static/html/errors/500.html")


def setup_middlewares(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("."))
    app.router.add_static("/static", "static")

    app.middlewares.append(error_middleware)
