class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []

        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            ans.append(word)

            if i != 0:
                ans.append(" ")

        return "".join(ans)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
