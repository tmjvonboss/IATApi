from .Api import AsyncApi, SyncApi
import aiofiles


class AsyncClient(AsyncApi):

    def __init__(self, key, package, certificate):
        AsyncApi.__init__(self, key=key, package=package, certificate=certificate)

    async def detect_label(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="LABEL_DETECTION", image=await f.read())

    async def detect_web(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="WEB_DETECTION", image=await f.read())

    async def detect_text(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="TEXT_DETECTION", image=await f.read())

    async def detect_logo(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="LOGO_DETECTION", image=await f.read())

    async def detect_landmark(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="LANDMARK_DETECTION", image=await f.read())

    async def detect_face(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="FACE_DETECTION", image=await f.read())

    async def detect_safe_search(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="SAFE_SEARCH_DETECTION", image=await f.read())

    async def image_property(self, path):
        async with aiofiles.open(path, "rb") as f:
            return await self.do(action="IMAGE_PROPERTIES", image=await f.read())

    async def close(self):
        return await self.session.close()


class SyncClient(SyncApi):

    def __init__(self, key, package, certificate):
        SyncApi.__init__(self, key=key, package=package, certificate=certificate)

    def detect_label(self, path):
        with open(path, "rb") as f:
            return self.do(action="LABEL_DETECTION", image=f.read())

    def detect_web(self, path):
        with open(path, "rb") as f:
            return self.do(action="WEB_DETECTION", image=f.read())

    def detect_text(self, path):
        with open(path, "rb") as f:
            return self.do(action="TEXT_DETECTION", image=f.read())

    def detect_logo(self, path):
        with open(path, "rb") as f:
            return self.do(action="LOGO_DETECTION", image=f.read())

    def detect_landmark(self, path):
        with open(path, "rb") as f:
            return self.do(action="LANDMARK_DETECTION", image=f.read())

    def detect_face(self, path):
        with open(path, "rb") as f:
            return self.do(action="FACE_DETECTION", image=f.read())

    def detect_safe_search(self, path):
        with open(path, "rb") as f:
            return self.do(action="SAFE_SEARCH_DETECTION", image=f.read())

    def image_property(self, path):
        with open(path, "rb") as f:
            return self.do(action="IMAGE_PROPERTIES", image=f.read())

    def close(self):
        self.session.close()
