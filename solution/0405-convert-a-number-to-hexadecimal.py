class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num_to_hex = {}
        for i in range(10):
            num_to_hex[i] = str(i)

        for i, ch in zip(range(10, 16), "abcdef"):
            num_to_hex[i] = ch

        digits = []

        if num < 0:
            num += 2**32

        while num > 0:
            digits.append(num % 16)
            num = num // 16

        ans = ""

        for digit in digits:
            ans += num_to_hex[digit]

        return ans[::-1]
