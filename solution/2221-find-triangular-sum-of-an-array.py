class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        def dfs(ns):
            if len(ns) == 1:
                return sum(ns)

            tmp = []
            for i in range(1, len(ns)):
                tmp.append((ns[i - 1] + ns[i]) % 10)

            return dfs(tmp)

        return dfs(nums)
