# Two Pointer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        l = 0
        r = len(str_x) - 1

        while l < r:
            if str_x[l] != str_x[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        original_x = x

        while x > 0:
            reversed_x = reversed_x * 10 + (x % 10)
            x = x // 10

        return reversed_x == original_x
