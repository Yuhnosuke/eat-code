class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        res = ""

        for st in strs:
            length = len(st)
            encoded = str(length) + delimiter + st

            res += encoded

        return res

    def decode(self, s: str) -> List[str]:
        delimiter = "#"
        res = []
        start = 0

        while start < len(s):
            end = start

            while s[end] != delimiter:
                end += 1

            length = s[start:end]

            start = end + 1
            end = start + int(length)

            res.append(s[start:end])

            start = end

        return res
