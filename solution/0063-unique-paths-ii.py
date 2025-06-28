# top down
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        def dp(r, c, memo):
            if r == rows or c == columns:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == columns - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            down = dp(r + 1, c, memo)
            right = dp(r, c + 1, memo)

            memo[(r, c)] = down + right
            return memo[(r, c)]

        return dp(0, 0, {})


# bottom up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][columns - 1] == 1:
            return 0

        dp = [[0] * (columns + 1) for _ in range(rows + 1)]
        dp[rows - 1][columns - 1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]
