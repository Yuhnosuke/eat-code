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
