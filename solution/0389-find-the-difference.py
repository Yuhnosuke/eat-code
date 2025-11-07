class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for s_ch, t_ch in zip(sorted(s), sorted(t)):
            if s_ch != t_ch:
                return t_ch
        return sorted(t)[-1]
