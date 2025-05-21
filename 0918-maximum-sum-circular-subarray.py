# brute force
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]

        for i in range(n):
            curr_sum = 0

            for j in range(i, i + n):
                curr_sum += nums[j % n]
                max_sum = max(max_sum, curr_sum)
        return max_sum


# kadane's algorithm
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]

        local_max = 0
        local_min = 0

        total = 0

        for num in nums:
            local_max = max(local_max + num, num)
            local_min = min(local_min + num, num)

            global_max = max(global_max, local_max)
            global_min = min(global_min, local_min)

            total += num

        if global_max > 0:
            return max(global_max, total - global_min)

        return global_max
