class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        non_zeros = sum(1 for x in nums if x > 0)

        def is_valid(nums: int, non_zeros: int, start: int, direction: int) -> bool:
            copied = nums.copy()
            curr = start

            while non_zeros > 0 and 0 <= curr < len(nums):
                if copied[curr] > 0:
                    copied[curr] -= 1
                    direction *= -1

                    if copied[curr] == 0:
                        non_zeros -= 1
                curr += direction
            return non_zeros == 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if is_valid(nums, non_zeros, i, -1):
                    ans += 1
                if is_valid(nums, non_zeros, i, 1):
                    ans += 1

        return ans
