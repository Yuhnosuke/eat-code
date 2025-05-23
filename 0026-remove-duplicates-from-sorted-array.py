from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        n = len(nums)

        while r < n:
            nums[l] = nums[r]

            while r < n and nums[l] == nums[r]:
                r += 1

            l += 1

        return l
