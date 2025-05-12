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
