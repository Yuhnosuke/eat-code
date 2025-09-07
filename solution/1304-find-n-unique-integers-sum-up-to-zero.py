class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        ans = []
        if n % 2:
            ans.append(0)

        origin_n = n

        while n:
            ans.append(n)
            ans.append(-n)

            n -= 1

            if len(ans) == origin_n:
                break

        return ans
