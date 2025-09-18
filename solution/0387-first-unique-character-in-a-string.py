class Solution:
    def firstUniqChar(self, s: str) -> int:
        ch_to_freq = {}
        for ch in s:
            if ch not in ch_to_freq:
                ch_to_freq[ch] = 0
            ch_to_freq[ch] += 1

        for i, ch in enumerate(s):
            if ch_to_freq[ch] == 1:
                return i
        return -1
