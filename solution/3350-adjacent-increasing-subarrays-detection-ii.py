class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        inc_end = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_end[i] = inc_end[i - 1] + 1
            else:
                inc_end[i] = 1

        def is_adj(k):
            for a in range(0, n - 2 * k + 1):
                if inc_end[a + k - 1] >= k and inc_end[a + 2 * k - 1] >= m:
                    return True
            return False

        l, r = 1, n // 2
        while l <= r:
            m = (l + r) // 2

            if is_adj(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans
