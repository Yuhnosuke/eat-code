class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1

        for i in range(len(word) - 1):
            curr_ch = word[i]
            next_ch = word[i + 1]

            if curr_ch == next_ch:
                ans += 1

        return ans
