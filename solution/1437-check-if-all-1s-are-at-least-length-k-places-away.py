class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j < len(nums) and j - i - 1 < k:
                    return False
        return True
