# top down1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp(i: int, curr_amount: int) -> int:
            if curr_amount == 0:
                return 0

            if i == len(coins):
                return float("inf")

            if curr_amount < 0:
                return float("inf")

            if (i, curr_amount) in memo:
                return memo[(i, curr_amount)]

            not_take = dp(i + 1, curr_amount)
            take = 1 + dp(i, curr_amount - coins[i])

            memo[(i, curr_amount)] = min(not_take, take)
            return memo[(i, curr_amount)]

        memo = {}
        ans = dp(0, amount)
        return ans if ans != float("inf") else -1


# top down2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp(curr_amount: int) -> int:
            if curr_amount == 0:
                return 0

            if curr_amount in memo:
                return memo[curr_amount]

            res = float("inf")

            for coin in coins:
                if curr_amount - coin >= 0:
                    res = min(res, 1 + dp(curr_amount - coin))

            memo[curr_amount] = res
            return memo[curr_amount]

        memo = {}
        ans = dp(amount)
        return ans if ans != float("inf") else -1


# top down 3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(remain_amount: int) -> int:
            if remain_amount == 0:
                return 0

            if remain_amount < 0:
                return -1

            if remain_amount in memo:
                return memo[remain_amount]

            min_cost = float("inf")
            memo[remain_amount] = min_cost

            for coin in coins:
                res = dp(remain_amount - coin)

                if res != -1:
                    min_cost = min(min_cost, res + 1)
                    memo[remain_amount] = min_cost

            return min_cost if min_cost != float("inf") else -1

        memo = {}
        return dp(amount)


# bottom up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        ans = dp[-1]
        return dp[-1] if ans != float("inf") else -1
