class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(i):
            # base case
            if i == len(nums):
                ans.append(curr.copy())
                return

            # include
            curr.append(nums[i])
            backtrack(i + 1)

            # not include
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        nums.sort()
        backtrack(0)
        return ans
