class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday_saving = 1

        while n > 0:
            for day in range(min(n, 7)):
                ans += monday_saving + day
            monday_saving += 1
            n -= 7

        return ans
