from aiohttp import web
import json


class java_util(web.Application):
    def __init__(self, app):
        self.app = app

    # /convertHashmapJson
    async def convertHashmapJson(self, request):
        if "hashmap" in request.query:
            rs_json = {}
            hashmap = request.query["hashmap"].replace("{", "").replace(
                "}", "").replace(", ", ",")
            for pair in hashmap.split(","):
                key, value = pair.split("=")
                rs_json[key] = value

            return web.json_response(rs_json)

        elif "json" in request.query:
            rs_json = json.loads(request.query["json"])
            hashmap = "{"
            for key in rs_json:
                hashmap += f"{key}={rs_json[key]}"
            print(rs_json)
            if hashmap[-1] == ",":
              hashmap = hashmap[:-1]
            hashmap = hashmap + "}"
            return web.Response(text=hashmap)
# shit school started, ill be in 40 min
        else:
            return web.FileResponse("./static/html/docs/index.html")

    async def something(self, request):
      return {"name": "test"}


def setup(app):
    return java_util(app), {"convertHashmapJson": "/convertHashmapJson", "something": "/something"}
