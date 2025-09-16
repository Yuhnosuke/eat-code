class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        ans = []
        for i in range(1, n):
            if i > n:
                break
            ans.append(i)
            n -= i

        return len(ans)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) // 2)
