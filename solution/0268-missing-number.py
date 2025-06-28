class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            ans = ans ^ nums[i] ^ i

        ans = ans ^ n
        return ans
