class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n: int) -> int:
            if n in memo:
                return memo[n]

            memo[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
            return memo[n]

        memo = {0: 0, 1: 1, 2: 1}
        return helper(n)


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]

        for num in range(3, n + 1):
            dp.append(dp[num - 3] + dp[num - 2] + dp[num - 1])

        return dp[n]
