class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            num_to_index[nums[i]] = i

        for i in range(len(nums)):
            finding = target - nums[i]
            if finding in num_to_index and num_to_index[finding] != i:
                return [i, num_to_index[finding]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_to_i = {}

        for i, num in enumerate(nums):
            finding = target - num
            if finding in prev_to_i:
                return [prev_to_i[finding], i]
            prev_to_i[num] = i
