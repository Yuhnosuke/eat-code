# top down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i: int) -> int:
            if i < 2:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(
                dp(i - 2) + cost[i - 2],
                dp(i - 1) + cost[i - 1],
            )

            return memo[i]

        memo = {}
        return dp(len(cost))


# bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[len(cost)]
