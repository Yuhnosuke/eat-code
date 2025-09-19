class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        ans = 0

        for c in range(columns):
            for r in range(1, rows):

                if grid[r][c] <= grid[r - 1][c]:
                    ans += grid[r - 1][c] + 1 - grid[r][c]
                    grid[r][c] = grid[r - 1][c] + 1

        return ans
