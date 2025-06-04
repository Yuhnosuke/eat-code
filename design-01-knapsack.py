# brute force
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dp(i, curr_capacity):
            if i == len(profit):
                return 0

            not_include = dp(i + 1, curr_capacity)
            include = (
                profit[i] + dp(i + 1, curr_capacity + weight[i])
                if curr_capacity + weight[i] <= capacity
                else 0
            )

            return max(not_include, include)

        return dp(0, 0)


# top down
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dp(i, curr_capacity, memo):
            if i == len(profit):
                return 0

            if memo[i][curr_capacity] != -1:
                return memo[i][curr_capacity]

            not_include = dp(i + 1, curr_capacity, memo)
            include = (
                profit[i] + dp(i + 1, curr_capacity + weight[i], memo)
                if curr_capacity + weight[i] <= capacity
                else 0
            )

            memo[i][curr_capacity] = max(not_include, include)

            return memo[i][curr_capacity]

        memo = [[-1] * (capacity + 1) for _ in range(len(profit))]
        return dp(0, 0, memo)


# bottom up
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]

        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = weight[0]

        for i in range(len(profit)):
            for c in range(capacity + 1):
                # not include
                not_include = dp[i - 1][c]

                # include
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][c - weight[i]]

                dp[i][c] = max(not_include, include)

        return dp[-1][-1]
