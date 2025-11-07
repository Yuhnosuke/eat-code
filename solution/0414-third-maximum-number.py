class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(num_set) < 3:
            return max(num_set)
        return sorted(list(num_set), reverse=True)[2]
