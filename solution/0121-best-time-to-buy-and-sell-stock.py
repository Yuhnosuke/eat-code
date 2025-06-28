class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0

        n = len(prices)
        profit = float("-inf")

        while r < n:
            while prices[l] > prices[r]:
                l += 1

            profit = max(profit, prices[r] - prices[l])

            r += 1

        return profit
