# brute force
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    ans += 1
                    continue

        return ans


from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_freq_map = defaultdict(int)
        sum_freq_map[0] += 1
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            ans += sum_freq_map[curr_sum - k]

            sum_freq_map[curr_sum] += 1

        return ans
