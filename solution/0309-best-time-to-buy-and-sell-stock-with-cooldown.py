class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i: int, is_buying: bool):

            if i >= len(prices):
                return 0

            if (i, is_buying) in memo:
                return memo[(i, is_buying)]

            cooldown = dfs(i + 1, is_buying)

            if is_buying:
                buy = dfs(i + 1, not is_buying) - prices[i]
                memo[(i, is_buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not is_buying) + prices[i]
                memo[(i, is_buying)] = max(sell, cooldown)

            return memo[(i, is_buying)]

        memo = {}
        return dfs(0, True)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i: int, is_holding: bool, is_cooldown: bool) -> int:
            # base case
            if i == len(prices):
                return 0

            if (i, is_holding, is_cooldown) in memo:
                return memo[(i, is_holding, is_cooldown)]

            if is_cooldown:
                # do nothing
                answer = dp(i + 1, is_holding, False)
            else:
                # do nothing
                answer = dp(i + 1, is_holding, False)

                if is_holding:
                    # sell
                    answer = max(answer, +prices[i] + dp(i + 1, False, True))
                else:
                    # buy
                    answer = max(answer, -prices[i] + dp(i + 1, True, False))

            memo[(i, is_holding, is_cooldown)] = answer
            return answer

        memo = {}
        return dp(0, False, False)
