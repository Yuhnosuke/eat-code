class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_n = []
        while n > 0:
            binary_n.append(n % 2)
            n = n // 2

        ans, digit = 0, 0
        for bn in binary_n:
            ans += 2**digit
            digit += 1
        return ans


class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while ans < n:
            ans = ans * 2 + 1
        return ans
