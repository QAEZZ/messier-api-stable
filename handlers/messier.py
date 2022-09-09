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
			print(response.query["object"])
			if "format" in response.query:
				print(response.query["format"])
				if response.query[
				    "format"] == "xml" or "html" or "yaml" or "visual":
					messier = messiers.get(object=response.query["object"],
					                       format=response.query["format"])

					if response.query["format"] == "visual":
						return web.Response(text=messier, content_type="html")
					else:
						return web.Response(text=messier)
			else:
				messier = messiers.get(object=response.query["object"])
				return web.json_response(messier)

		else:
			return web.FileResponse('./static/html/docs/index.html')

# /random

	async def random(self, response):
		"""
        get random object ☄️
          - /messier/random
        """
		if "format" in response.query:
			print(response.query["format"])
			if response.query[
			    "format"] == "xml" or "html" or "yaml" or "visual":
				messier = messiers.get(object=random.randint(1, 110),
				                       format=response.query["format"])

				if response.query["format"] == "visual":
					return web.Response(text=messier, content_type="html")
				else:
					return web.Response(text=messier)
		else:
			messier = messiers.get(object=response.query["object"])
			return web.json_response(messier)


# /all

	async def all(self, response):
		"""
      get all objects
        - /messier/all
      """
		with open("./data/messier.json", "r") as f:
			data = json.load(f)
			return web.json_response(data)


def setup(app):
	return _messier(app), {
	    "messier": "/messier",
	    "random": "/messier/random",
	    "all": "/messier/all"
	}
