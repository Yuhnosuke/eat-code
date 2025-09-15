class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0

        for word in text.split():
            tmp = 0
            for letter in brokenLetters:
                if letter in word:
                    tmp += 1
            if not tmp:
                ans += 1
        return ans
