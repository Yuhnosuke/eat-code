# top down
class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n, memo):
            if n <= 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = f(n - 1, memo) + f(n - 2, memo)
            return memo[n]

        return f(n, {})


# bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


# bottom up(space optimized)
class Solution:
    def climbStairs(self, n: int) -> int:
        one_back = 1
        two_back = 1

        for i in range(2, n + 1):
            tmp = one_back
            one_back = two_back + one_back
            two_back = tmp

        return one_back
