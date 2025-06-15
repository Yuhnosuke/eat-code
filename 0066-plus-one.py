class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1

        while p > -1:
            if digits[p] + 1 != 10:
                digits[p] += 1
                return digits

            digits[p] = 0
            p -= 1

        return [1] + digits
