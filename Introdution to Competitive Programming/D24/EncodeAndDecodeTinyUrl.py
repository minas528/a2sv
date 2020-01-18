class Codec:
    def __init__(self):
        self.lst = {}
        self.main = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        import random
        samp = "abcdefghijklmnopqrstuvwxyz1234567890"
        code = ""
        for i in range(10):
            code += random.choice(samp)
        code = self.main + code
        # print(code)
        if code not in self.lst:
            self.lst[code] = longUrl
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if self.lst[shortUrl] is not None:
            # print(self.lst[shortUrl])
            return self.lst[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
