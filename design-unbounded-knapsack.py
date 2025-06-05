# top down
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # i番目までのitemでcurr_capacityで作れる最大profit
        def dp(i: int, curr_capacity: int) -> int:
            if i == len(profit):
                return 0

            if (i, curr_capacity) in memo:
                return memo[(i, curr_capacity)]

            not_take = dp(i + 1, curr_capacity)

            take = 0
            if curr_capacity - weight[i] >= 0:
                take = profit[i] + dp(i, curr_capacity - weight[i])

            memo[(i, curr_capacity)] = max(not_take, take)
            return max(not_take, take)

        memo = {}
        return dp(0, capacity)


# bottom up
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]
        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for p in range(len(profit)):
            for c in range(capacity + 1):
                # skip
                dp[p][c] = dp[p - 1][c]
                # take
                if c - weight[p] >= 0:
                    dp[p][c] = max(profit[p] + dp[p][c - weight[p]], dp[p][c])

        return dp[len(profit) - 1][capacity]
