class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index_stack = [-1]
        ans = 0

        for i in range(len(heights)):
            while index_stack[-1] != -1 and heights[i] <= heights[index_stack[-1]]:
                height = heights[index_stack.pop()]
                width = i - index_stack[-1] - 1
                ans = max(ans, height * width)

            index_stack.append(i)

        while index_stack[-1] != -1:
            height = heights[index_stack.pop()]
            width = len(heights) - index_stack[-1] - 1
            ans = max(ans, height * width)

        return ans
