class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            left_prefix_sum.append(left_prefix_sum[-1] + nums[i])

        reversed_nums = list(reversed(nums))
        right_prefix_sum = [reversed_nums[0]]

        for i in range(1, len(reversed_nums)):
            right_prefix_sum.append(right_prefix_sum[-1] + reversed_nums[i])

        right_prefix_sum.reverse()

        for i in range(len(nums)):
            if left_prefix_sum[i] == right_prefix_sum[i]:
                return i

        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        right_total = total - left_total

        for i in range(len(nums)):
            left_total += nums[i]

            if left_total == right_total:
                return i

            right_total = total - left_total

        return -1
