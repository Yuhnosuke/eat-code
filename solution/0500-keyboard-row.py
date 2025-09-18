class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphabets_by_row = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]

        ans = []

        for alphabet_by_row in alphabets_by_row:
            for word in words:
                can_be_typed = True

                for ch in word:
                    if ch.lower() not in alphabet_by_row:
                        can_be_typed = False

                if can_be_typed:
                    ans.append(word)

        return ans
