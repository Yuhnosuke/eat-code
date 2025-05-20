# top down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        columns = n

        def dp(r, c, memo):
            if r == rows or c == columns:
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
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        columns = n

        dp = [[0] * columns for _ in range(rows)]

        dp[rows - 1][columns - 1] = 1

        for c in range(columns):
            dp[rows - 1][c] = 1
        for r in range(rows):
            dp[r][columns - 1] = 1

        for r in range(rows - 2, -1, -1):
            for c in range(columns - 2, -1, -1):
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

        return dp[0][0]


# bottom up(space optimized)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        columns = n

        prev_row = [1] * columns

        for r in range(rows - 1):
            current_row = [1] * columns

            for c in range(columns - 2, -1, -1):
                current_row[c] = current_row[c + 1] + prev_row[c]

            prev_row = current_row

        return prev_row[0]
