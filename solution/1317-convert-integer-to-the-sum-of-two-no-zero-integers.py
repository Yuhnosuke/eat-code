class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def has_no_zero(num):
            while num:
                if num % 10 == 0:
                    return False
                num = num // 10
            return True

        for a in range(1, n):
            if has_no_zero(a) and has_no_zero(n - a):
                return [a, n - a]
