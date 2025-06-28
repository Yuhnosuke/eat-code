# top down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i, j, memo):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1, memo)

            memo[(i, j)] = max(dp(i + 1, j, memo), dp(i, j + 1, memo))

            return memo[(i, j)]

        return dp(0, 0, {})


# bottom up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        columns = len(text2)
        dp = [[0] * (columns + 1) for _ in range(rows + 1)]

        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]


# bottom up(space optimized)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        columns = len(text2)

        curr = [0] * (columns + 1)
        prev = [0] * (columns + 1)

        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                if text1[r] == text2[c]:
                    curr[c] = 1 + prev[c + 1]
                else:
                    curr[c] = max(curr[c + 1], prev[c])
            curr, prev = prev, curr

        return prev[0]
