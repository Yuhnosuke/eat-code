class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindromic_string = ""
        length = 0

        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    longest_palindromic_string = s[l : r + 1]
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    longest_palindromic_string = s[l : r + 1]
                l -= 1
                r += 1

        return longest_palindromic_string
