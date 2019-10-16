class URL_shortener:
    def __init__(self):
        self.url_id = {}
        self.id = 1000000

    def shorten_url(self, original_url):
        if original_url in self.url_id:
            self.id = self.url_id[original_url]
            shorten_url = self.encode(self.id)
            self.id += 1

        else:
            self.url_id[original_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1

        return "short_url.com/"+str(shorten_url)

    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base62 = len(characters)

        ret = []
        while id > 0:
            val = id % base62
            ret.append(characters[val])
            id = id // base62

        return "".join(ret[::-1])

shortener = URL_shortener()
print(shortener.shorten_url("https://www.youtube.com/watch?v=_28Kei8hhF0"))
