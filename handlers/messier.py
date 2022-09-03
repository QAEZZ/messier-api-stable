# ill create a seperate file for the JSON dump k

from aiohttp import web
import messiers
import json
import _config_
import logging
import random

logging.basicConfig(filename='log.log', level=logging.DEBUG)

class _messier(web.Application):
    def __init__(self, app):
        self.app = app

    # /messier
    async def messier(self, response):

        if "object" in response.query:
            print("object in query")
            # send DSO by messier number
            messier = messiers.get(object=response.query["object"])
            print(f"object pre-get is {messier}")
            return web.json_response(messier)
        elif "random" in response.query and response.query["random"].lower(
        ) == "true":
            # send a random object
            messier = messiers.get()
            return web.json_response(messier)

        else:
            return web.FileResponse('./static/html/docs/index.html')

    # /random
    async def random(self, response):
        """
        get random object ☄️
          - /messier/random
        """
        messier = messiers.get(random.randint(1,110))
        return web.json_response(messier)



def setup(app):
    return _messier(app), {
        "messier": "/messier",
        "random": "/messier/random"
    }
