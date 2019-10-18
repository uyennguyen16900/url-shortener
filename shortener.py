import string
from random import randint

class URL_shortener:
    def __init__(self):
        self.url_id = {}
        self.id = randint(1, 100000000)

    def shorten_url(self, original_url):
        """Shorten the original url"""
        if original_url in self.url_id:
            self.id = self.url_id[original_url]
            shorten_url = self.encode(self.id)

        else:
            self.url_id[original_url] = self.id
            shorten_url = self.encode(self.id)

        return str(shorten_url)

    def encode(self, id):
        """Generate string using base62"""
        characters = string.digits + string.ascii_letters
        base62 = len(characters)

        ret = []
        while id > 0:
            val = id % base62
            ret.append(characters[val])
            id = id // base62

        return "".join(ret[::-1])

if __name__ == "__main__":
    shortener = URL_shortener()
    print(shortener.shorten_url("https://www.youtube.com/watch?v=_28Kei8hhF0"))
    print(shortener.shorten_url("https://github.com/uyennguyen16900/Captain-Rainbow"))
