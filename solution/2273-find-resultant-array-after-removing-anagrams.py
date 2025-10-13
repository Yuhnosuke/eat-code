class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]

        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                ans.append(words[i])

        return ans


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        frequencies = [Counter(word) for word in words]
        ans = [words[0]]

        for i in range(1, len(words)):
            if frequencies[i] != frequencies[i - 1]:
                ans.append(words[i])

        return ans
