class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        curr = []

        def backtrack(i):
            if len(curr) == len(digits):
                if curr:
                    ans.append("".join(curr.copy()))
                return

            for letter in digit_to_letter[digits[i]]:
                curr.append(letter)
                backtrack(i + 1)

                curr.pop()

        backtrack(0)
        return ans
