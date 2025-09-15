class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        return 1 + (num - 1) % 9


class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num < 10:
                return num

            a = num // 10
            b = num % 10

            num = a + b
