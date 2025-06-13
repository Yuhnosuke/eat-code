class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) >> 1
            a = a ^ b
            b = carry

        return a


Solution().getSum(2, 3)
