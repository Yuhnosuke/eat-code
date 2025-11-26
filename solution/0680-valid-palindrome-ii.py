class Solution:
    def validPalindrome(self, s: str) -> bool:

        def dfs(l, r, count):

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if count == 0:
                        return False
                    return dfs(l, r - 1, count - 1) or dfs(l + 1, r, count - 1)

            return True

        return dfs(0, len(s) - 1, 1)
