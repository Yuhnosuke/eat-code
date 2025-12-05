class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if (left - right) % 2 == 0:
                count += 1
        return count


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 2:
            return 0
        return len(nums) - 1
