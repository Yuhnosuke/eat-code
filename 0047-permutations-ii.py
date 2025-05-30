class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = []
        curr = []

        added_indices = []

        def backtrack():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for i in range(len(nums)):

                if i in added_indices:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in added_indices:
                    continue

                curr.append(nums[i])
                added_indices.append(i)

                backtrack()
                curr.pop()
                added_indices.pop()

        nums.sort()
        backtrack()
        return ans
