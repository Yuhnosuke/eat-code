class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 1
        len_n = 1
        seen_remainders = set()

        while remainder % k != 0:
            n = remainder * 10 + 1
            remainder = n % k
            len_n += 1

            if remainder in seen_remainders:
                return -1
            else:
                seen_remainders.add(remainder)

        return len_n


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for len_n in range(1, k + 1):
            remainder = (10 * remainder + 1) % k
            if remainder == 0:
                return len_n
        return -1
