class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num

        while l <= r:
            m = (l + r) // 2
            product = m * m

            if product == num:
                return True
            elif product > num:
                r = m - 1
            else:
                l = m + 1

        return False
