# top down
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, curr_sum):
            if i == len(nums) and curr_sum == target:
                return 1

            if i == len(nums):
                return 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            # add
            add = dp(i + 1, curr_sum + nums[i])

            # subtrack
            subtract = dp(i + 1, curr_sum - nums[i])

            memo[(i, curr_sum)] = add + subtract

            return memo[(i, curr_sum)]

        memo = {}
        return dp(0, 0)


# bottom up
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # row: index, col: curr_sum
        # dp[r][c]: count
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i + 1][curr_sum + nums[i]] += count
                dp[i + 1][curr_sum - nums[i]] += count

        return dp[len(nums)][target]
