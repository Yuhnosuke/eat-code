class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1

        for i in range(2, len(num)):
            a, b, c = num[i - 2], num[i - 1], num[i]

            if a == b and b == c:
                ans = max(ans, int(a))

        return "" if ans == -1 else str(ans) * 3
