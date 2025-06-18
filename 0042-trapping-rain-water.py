# Two Pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        left_max = height[l]
        right_max = height[r]

        ans = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                ans += right_max - height[r]

        return ans


# Brute Force
# Time Limit Exceeded
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        for i in range(len(height)):
            left_max = height[i]
            for l in range(i):
                left_max = max(left_max, height[l])

            right_max = height[i]
            for r in range(i + 1, len(height)):
                right_max = max(right_max, height[r])

            ans += min(left_max, right_max) - height[i]

        return ans
