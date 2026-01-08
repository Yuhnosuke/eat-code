class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        ans = 0

        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                if grid[r][c] >= 0:
                    break
                ans += 1
        return ans
