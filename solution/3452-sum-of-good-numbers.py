class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):

            # case: neither of i - k, i + k exists
            if i - k < 0 and i + k >= len(nums):
                ans += nums[i]
                continue

            # case: i - k doesn't exist
            if i - k < 0 and nums[i] > nums[i + k]:
                ans += nums[i]
                continue

            # case: i + k doesn't exist
            if i + k >= len(nums) and nums[i] > nums[i - k]:
                ans += nums[i]
                continue

            # # case: both of i - k, i + k exists
            if nums[i - k] < nums[i] > nums[i + k]:
                ans += nums[i]
                continue

        return ans
