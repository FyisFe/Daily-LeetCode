from random import choice


class Codec:
    def __init__(self):
        self.charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.urls = {}

    def get_key(self):
        return "".join(choice(self.charset) for i in range(6))

    def encode(self, longUrl: str) -> str:
        key = self.get_key()
        while key in self.urls:
            key = self.get_key()
        self.urls[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl[-6:]
        if key in self.urls:
            return self.urls[key]
        return ""
