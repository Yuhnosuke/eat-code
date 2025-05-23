class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])

        reversed_nums = list(reversed(nums))
        suffix = [reversed_nums[0]]
        for i in range(1, len(reversed_nums)):
            suffix.append(suffix[-1] * reversed_nums[i])
        suffix.reverse()

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix[i + 1])
            elif i == len(nums) - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * suffix[i + 1])

        return ans
