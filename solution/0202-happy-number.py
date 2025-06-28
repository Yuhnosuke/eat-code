class Solution:
    def isHappy(self, n: int) -> bool:

        def digitify(n: int) -> List[int]:
            res = []

            while n > 0:
                res.append(n % 10)
                n = n // 10

            return res

        def sum_square(nums: List[int]) -> int:
            total = 0
            for num in nums:
                total += num**2
            return total

        def is_happy(num):
            return num == 1

        seen = set()

        while True:
            if is_happy(n):
                return True

            if n in seen:
                return False

            seen.add(n)

            n = sum_square(digitify(n))
