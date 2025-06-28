class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            m = (l + r) // 2

            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            m = (l + r) // 2

            if nums[m] < nums[l]:
                l += 1
                r = m

            elif nums[l] > nums[r]:
                l = m + 1

            elif nums[l] < nums[r]:
                r = m - 1

        return nums[l]
