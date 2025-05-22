from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = defaultdict(int)

        for ch in s:
            freq_map[ch] += 1

        for ch in t:
            freq_map[ch] -= 1

        return all(freq == 0 for freq in freq_map.values())
