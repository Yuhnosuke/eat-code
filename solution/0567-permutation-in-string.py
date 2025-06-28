class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ch_to_freq = {}

        for ch in s1:
            if ch not in ch_to_freq:
                ch_to_freq[ch] = 0
            ch_to_freq[ch] += 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in ch_to_freq:
                ch_to_freq[s2[r]] -= 1

            while r - l + 1 > len(s1):
                if s2[l] in ch_to_freq:
                    ch_to_freq[s2[l]] += 1
                l += 1

            if all(value == 0 for value in ch_to_freq.values()):
                return True

        return False
