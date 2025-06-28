class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        ans = ""

        for i in range(min_len):
            ans += word1[i]
            ans += word2[i]

        if min_len == len(word1):
            ans += word2[i + 1 :]
        if min_len == len(word2):
            ans += word1[i + 1 :]

        return ans
