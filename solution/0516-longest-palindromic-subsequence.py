class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0

            if l == r:
                return 1

            if (l, r) in memo:
                return memo[(l, r)]

            if s[l] == s[r]:
                memo[(l, r)] = dp(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(dp(l + 1, r), dp(l, r - 1))

            return memo[(l, r)]

        memo = {}

        return dp(0, len(s) - 1)
