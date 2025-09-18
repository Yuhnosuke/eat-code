class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        l, r = 0, n - 1

        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                l = i
                break

        if l == 0:
            return False

        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                r = i
                break

        if r == n - 1:
            return False

        for i in range(l, r):
            if nums[i] <= nums[i + 1]:
                return False

        return True
