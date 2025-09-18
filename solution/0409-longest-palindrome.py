class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_to_freq = {}

        for ch in s:
            if ch not in ch_to_freq:
                ch_to_freq[ch] = 0
            ch_to_freq[ch] += 1

        ans = 0
        has_odd = False

        for freq in ch_to_freq.values():
            ans += freq // 2 * 2
            if freq % 2 == 1:
                has_odd = True

        if has_odd:
            ans += 1
        return ans
