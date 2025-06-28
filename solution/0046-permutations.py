# time complexity: O(n * n!), space complexity: O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack()

                    curr.pop()

        backtrack()
        return ans


# time complexity: O(n * n!), space complexity: O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums):
            if i == len(nums):
                return [[]]

            all_new_permutations = []
            sub_permutations = helper(i + 1, nums)

            for sub_permutation in sub_permutations:
                for j in range(len(sub_permutation) + 1):
                    new_permutation = sub_permutation.copy()
                    new_permutation.insert(j, nums[i])
                    all_new_permutations.append(new_permutation)

            return all_new_permutations

        return helper(0, nums)
