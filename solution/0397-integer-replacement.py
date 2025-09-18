class Solution:
    def integerReplacement(self, n: int) -> int:

        def dfs(n):
            if n == 1:
                return 0

            if n in memo:
                return memo[n]

            if n % 2:
                memo[n] = min(dfs(n + 1) + 1, dfs(n - 1) + 1)
            else:
                memo[n] = dfs(n // 2) + 1

            return memo[n]

        memo = {}
        return dfs(n)
