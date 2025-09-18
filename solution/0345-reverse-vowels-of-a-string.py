class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = "aiueoAIUEO"

        ans = list(s)
        while l < r:
            if ans[l] in vowels and ans[r] in vowels:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
            elif ans[l] not in vowels:
                l += 1
            elif ans[r] not in vowels:
                r -= 1

        return "".join(ans)
