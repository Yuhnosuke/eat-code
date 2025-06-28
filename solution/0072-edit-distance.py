# top down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dp(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(
                    # insert
                    dp(i, j + 1),
                    # delete
                    dp(i + 1, j),
                    # replace
                    dp(i + 1, j + 1),
                )

            return memo[(i, j)]

        memo = {}
        return dp(0, 0)


# bottom up
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # base case
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        # insert
                        dp[i + 1][j],
                        # delete
                        dp[i][j + 1],
                        # replace
                        dp[i + 1][j + 1],
                    )

        return dp[0][0]
