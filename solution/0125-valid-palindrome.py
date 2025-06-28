class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = ""
        for ch in s:
            if ch.isalnum():
                lower_s += ch.lower()

        l = 0
        r = len(lower_s) - 1

        while l < r:
            if lower_s[l] != lower_s[r]:
                return False

            l += 1
            r -= 1

        return True
