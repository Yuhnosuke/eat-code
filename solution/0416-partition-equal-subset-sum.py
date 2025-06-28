# top down
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        def dp(i: int, curr_sum: int, memo: List[Optional[bool]]) -> bool:
            if curr_sum == target:
                return True

            if i == len(nums):
                return False

            if curr_sum > target:
                return False

            if memo[i][curr_sum] is not None:
                return memo[i][curr_sum]

            not_take = dp(i + 1, curr_sum, memo)
            take = dp(i + 1, nums[i] + curr_sum, memo)

            memo[i][curr_sum] = not_take or take

            return memo[i][curr_sum]

        memo = [[None] * (target + 1) for _ in range(len(nums))]
        return dp(0, 0, memo)


# bottom up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for n in range(len(nums)):
            dp[n][0] = True

        for t in range(target + 1):
            if t == nums[0]:
                dp[0][t] = True

        for n in range(1, len(nums)):
            for t in range(target + 1):
                # not take
                not_take = dp[n - 1][t]

                # take
                if t - nums[n] >= 0:
                    take = dp[n - 1][t - nums[n]]
                    dp[n][t] = not_take or take
                else:
                    dp[n][t] = not_take

        return dp[-1][-1]
