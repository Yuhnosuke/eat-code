class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = 0
        vallies = 0

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1]:
                continue

            p = i - 1
            n = i + 1

            while p > 0 and nums[i] == nums[p]:
                p -= 1
            while n < len(nums) - 1 and nums[i] == nums[n]:
                n += 1

            if nums[p] < nums[i] and nums[i] > nums[n]:
                hills += 1

            if nums[p] > nums[i] and nums[i] < nums[n]:
                vallies += 1

        return hills + vallies
