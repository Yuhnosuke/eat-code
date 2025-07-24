class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for i in range(len(words)):
            word = words[i]
            if x in word:
                ans.append(i)

        return ans
