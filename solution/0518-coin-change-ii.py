# top down
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        def dp(i, curr_amount):
            if curr_amount == 0:
                return 1

            if i == len(coins):
                return 0

            if (i, curr_amount) in memo:
                return memo[(i, curr_amount)]

            ans = 0

            if curr_amount - coins[i] >= 0:
                ans = dp(i + 1, curr_amount)
                ans += dp(i, curr_amount - coins[i])

            memo[(i, curr_amount)] = ans

            return ans

        memo = {}
        return dp(0, amount)
