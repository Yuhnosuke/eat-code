from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = float("-inf")
        freq_map = defaultdict(int)

        for r in range(len(s)):
            freq_map[s[r]] += 1

            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
