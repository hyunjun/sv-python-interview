class Codec:
    def __init__(self):
        self.count = 0
        self.prefix = "http://tinyurl.com/"
        self.character = (
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
        self.table = {}

    def encode(self, longUrl: str) -> str:
        """URL을 단축 URL로 프로그래밍한다"""
        self.count += 1

        def ConvertBase62(count):
            strs = ""
            for _ in range(6):
                """숫자를 62진수(문자열)로 변환하는 과정"""
                strs = strs + self.character[count % 62]
                count = count // 62
            return strs

        shortUrl = ConvertBase62(self.count)
        self.table[shortUrl] = longUrl

        return self.prefix + shortUrl

    def decode(self, shortUrl: str) -> str:
        """단축 URL을 원래 URL로 디코딩한다"""
        if shortUrl[-6:] in self.table:
            return self.table[shortUrl[-6:]]
