# top down
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dp(i: int, curr_zeros: int, curr_ones: int, memo: dict) -> int:
            if i == len(strs):
                return 0

            if (i, curr_zeros, curr_ones) in memo:
                return memo[(i, curr_zeros, curr_ones)]

            zeros = 0
            ones = 0
            for ch in strs[i]:
                if ch == "0":
                    zeros += 1
                else:
                    ones += 1

            not_take = dp(i + 1, curr_zeros, curr_ones, memo)

            take = 0
            if curr_zeros + zeros <= m and curr_ones + ones <= n:
                take = 1 + dp(i + 1, curr_zeros + zeros, curr_ones + ones, memo)

            memo[(i, curr_zeros, curr_ones)] = max(not_take, take)
            return memo[(i, curr_zeros, curr_ones)]

        memo = {}
        return dp(0, 0, 0, memo)


## bottom up
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for ch in strs:
            zeros = ch.count("0")
            ones = ch.count("1")

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

        return dp[m][n]
