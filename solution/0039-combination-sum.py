class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if i == len(candidates) or sum(curr) > target:
                return

            if sum(curr) == target:
                res.append(curr.copy())
                return

            curr.append(candidates[i])
            backtrack(i, curr)

            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res
