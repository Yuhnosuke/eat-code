class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        i = 0

        while i < len(s):
            if s[i] == "1":
                j = i + 1
                while j < len(s) and s[j] == "1":
                    j += 1
                n = j - i
                ans += (n + 1) * n // 2
                i = j + 1
            else:
                i += 1
            
        return ans % (10 ** 9 + 7)

