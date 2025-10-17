class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ch_to_freq = {}

        for s_ch in s:
            if s_ch not in s_ch_to_freq:
                s_ch_to_freq[s_ch] = 0
            s_ch_to_freq[s_ch] += 1

        for t_ch in t:
            if t_ch not in s_ch_to_freq:
                return False

            s_ch_to_freq[t_ch] -= 1


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ch_to_freq = {}

        for s_ch in s:
            if s_ch not in s_ch_to_freq:
                s_ch_to_freq[s_ch] = 0
            s_ch_to_freq[s_ch] += 1

        for t_ch in t:
            if t_ch not in s_ch_to_freq or s_ch_to_freq[t_ch] == 0:
                return False
            s_ch_to_freq[t_ch] -= 1

        return True
        return not any(s_ch_to_freq.values())


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = defaultdict(int)

        for ch in s:
            freq_map[ch] += 1

        for ch in t:
            freq_map[ch] -= 1

        return all(freq == 0 for freq in freq_map.values())
