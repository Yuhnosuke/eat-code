class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_set = set(nums)
        sorted_nums = sorted(nums_set)
        filtered_nums = list(filter(lambda x: x > 0, sorted_nums))

        if not filtered_nums:
            return sorted_nums[-1]

        return sum(filtered_nums)
