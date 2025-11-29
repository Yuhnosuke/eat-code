class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        total = sum(nums)
        while total % k:
            total -= 1
            ans += 1
        return ans


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr_sum = sum(nums)

        if not curr_sum % k:
            return 0

        target = curr_sum // k * k
        return curr_sum - target
