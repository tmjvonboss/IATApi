import requests
import aiohttp
from .Constants import Constants
import base64
import json


class AsyncApi:

    def __init__(self, key, package, certificate):
        self.session = None
        self.constants = Constants(key=key, package=package, certificate=certificate)

    async def do(self, action, image, results=10):
        if self.session is None:
            self.session = aiohttp.ClientSession(headers=self.constants.headers)
        self.constants.request_body["requests"][0]["features"][0]["maxResults"] = results
        self.constants.request_body["requests"][0]["features"][0]["type"] = action
        self.constants.request_body["requests"][0]["image"]["content"] = base64.urlsafe_b64encode(image).decode("utf-8")
        async with self.session.post(url=self.constants.url, data=json.dumps(self.constants.request_body)) as r:
            return await r.json()


class SyncApi:

    def __init__(self, key=None, package=None, certificate=None):
        self.session = requests.Session()
        self.constants = Constants(key=key, package=package, certificate=certificate)
        self.session.headers = self.constants.headers

    def do(self, action, image, results=10):
        self.constants.request_body["requests"][0]["features"][0]["maxResults"] = results
        self.constants.request_body["requests"][0]["features"][0]["type"] = action
        self.constants.request_body["requests"][0]["image"]["content"] = base64.urlsafe_b64encode(image).decode("utf-8")
        return self.session.post(url=self.constants.url, data=json.dumps(self.constants.request_body)).json()
