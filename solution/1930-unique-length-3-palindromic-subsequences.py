class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        ch_to_idxs = {}

        for i in range(len(s)):
            if s[i] not in ch_to_idxs:
                ch_to_idxs[s[i]] = []
            ch_to_idxs[s[i]].append(i)

        for idxs in ch_to_idxs.values():
            if len(idxs) > 1:
                min_idx, max_idx = min(idxs), max(idxs)
                ans += len(set(s[min_idx + 1 : max_idx]))

        return ans
