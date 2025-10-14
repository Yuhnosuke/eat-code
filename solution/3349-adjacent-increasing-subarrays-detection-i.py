class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        inc_end = [1] * n

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc_end[i] = inc_end[i - 1] + 1
            else:
                inc_end[i] = 1

        for a in range(0, n - 2 * k + 1):
            if inc_end[a + k - 1] >= k and inc_end[a + 2 * k - 1] >= k:
                return True

        return False
