class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) > 2:
            curr_sum = ""
            for i in range(1, len(s)):
                prev, curr = int(s[i - 1]), int(s[i])
                curr_sum += str((prev + curr) % 10)
            s = curr_sum

        return s[0] == s[1]
