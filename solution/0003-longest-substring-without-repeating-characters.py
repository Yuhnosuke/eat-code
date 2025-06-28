class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ans = float("-inf")
        l = 0

        for r in range(len(s)):

            while s[r] in s[l:r]:
                l += 1

            curr_len = r - l + 1
            ans = max(ans, curr_len)

        return ans
