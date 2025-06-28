# top down
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = math.ceil(total / 2)

        def dp(i: int, curr_sum: int, memo: dict) -> int:
            if curr_sum >= target or i == len(stones):
                return abs(curr_sum - (total - curr_sum))

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            not_take = dp(i + 1, curr_sum, memo)
            take = dp(i + 1, curr_sum + stones[i], memo)

            memo[(i, curr_sum)] = min(not_take, take)
            return memo[(i, curr_sum)]

        memo = {}
        return dp(0, 0, memo)


# bottom up
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]

        for s in range(1, len(stones) + 1):
            for t in range(target + 1):
                if t >= stones[s - 1]:
                    dp[s][t] = max(
                        dp[s - 1][t], dp[s - 1][t - stones[s - 1]] + stones[s - 1]
                    )
                else:
                    dp[s][t] = dp[s - 1][t]

        return total - 2 * dp[len(stones)][target]
