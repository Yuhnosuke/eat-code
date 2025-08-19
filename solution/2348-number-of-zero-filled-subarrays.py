class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        contiguous = 0

        for num in nums:
            if num == 0:
                contiguous += 1
                ans += contiguous
            else:
                contiguous = 0

        return ans
