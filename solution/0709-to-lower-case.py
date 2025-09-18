class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch.isupper():
                ans += chr(ord(ch) + 32)
            else:
                ans += ch

        return ans
