class Solution:
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + self.delimiter + s
        return res

    def decode(self, s: str) -> List[str]:
        st = 0
        res = []

        while st < len(s):
            en = st

            while s[en] != self.delimiter:
                en += 1

            length = s[st:en]

            st = en + 1
            en = st + int(length)

            res.append(s[st:en])

            st = en

        return res
