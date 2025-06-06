# top down
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # daysのi番目以降の最小コストを返す
        def dp(i: int) -> int:
            if i == len(days):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = float("inf")

            # 1, 7, 30日のチケットを購入した時の次の開始dayを示すindex
            j = i

            for duration, cost in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1

                memo[i] = min(memo[i], cost + dp(j))

            return memo[i]

        memo = {}
        return dp(0)


# bottom up
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)

        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            j = 1

            for duration, cost in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1

                dp[i] = min(dp[i], cost + dp[j])

        return dp[0]
