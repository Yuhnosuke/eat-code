class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32bit mask
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # limit 32 bit
            carry = (a & b) & MASK
            # shift to left by 1 with limiting 32 bit
            carry = (carry << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        if a <= MAX_INT:
            return a
        else:
            # 2 complement
            return ~(a ^ MASK)
