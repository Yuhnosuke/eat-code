class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        ans = -1

        for i in range(1, len(nums)):
            min_num = min(min_num, nums[i])
            if nums[i] > min_num:
                ans = max(ans, nums[i] - min_num)

        return ans
