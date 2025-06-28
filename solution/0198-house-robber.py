# top down
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i, memo):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i - 2, memo), dp(i - 1, memo))
            return memo[i]

        return dp(len(nums) - 1, {})


# bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


# bottom up(space optimized)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        two_back = nums[0]
        one_back = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = one_back
            one_back = max(nums[i] + two_back, one_back)
            two_back = tmp

        return one_back
