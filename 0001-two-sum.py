class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            index_map[num] = i

        for i in range(len(nums)):
            current_num = nums[i]
            finding_num = target - current_num

            if finding_num in index_map and i != index_map[finding_num]:
                return [i, index_map[finding_num]]
