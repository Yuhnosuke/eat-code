class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha_to_vale = {}
        alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(len(alphas)):
            alpha_to_vale[alphas[i]] = i + 1

        ans, digit = 0, 0
        reversed_title = columnTitle[::-1]

        for i in range(len(reversed_title)):
            ans += alpha_to_vale[reversed_title[i]] * len(alphas) ** digit
            digit += 1

        return ans
