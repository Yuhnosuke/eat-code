class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        ans = float("-inf")

        while l < r:

            h = min(height[l], height[r])
            w = r - l

            curr_area = h * w

            ans = max(ans, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
