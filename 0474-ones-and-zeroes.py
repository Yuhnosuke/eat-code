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
