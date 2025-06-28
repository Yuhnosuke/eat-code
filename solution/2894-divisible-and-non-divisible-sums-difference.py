# brute force1
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = 0
        nums2 = 0

        for i in range(1, n + 1):
            if i % m:
                nums1 += i
            else:
                nums2 += i

        return nums1 - nums2


# brute force2
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            if i % m:
                ans += i
            else:
                ans -= i

        return ans


# brute force3
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(i if i % m else -i for i in range(1, n + 1))
