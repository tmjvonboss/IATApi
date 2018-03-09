CLIENT_VERSION = "1.23.0"


class Constants:

    def __init__(self, key=None, package=None, certificate=None):
        self.key = key
        self.package = package
        self.certificate = certificate
        self.headers = {
            "Accept-Encoding": "gzip",
            "User-Agent": "Google-API-Java-Client Google-HTTP-Java-Client/%s (gzip)" % CLIENT_VERSION,
            "x-android-package": self.package,
            "x-android-cert": self.certificate,
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "Keep-Alive"
        }
        self.url = "https://vision.googleapis.com/v1/images:annotate?key=%s" % self.key
        self.request_body = {"requests": [
            {
                "features": [
                    {
                        "maxResults": None,
                        "type": None
                    }
                ],
                "image": {
                    "content": None
                }
            }
        ]}
