class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # avoid duplication
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            finding_sum = 0 - nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                two_sum = nums[l] + nums[r]

                if two_sum < finding_sum:
                    l += 1
                elif two_sum > finding_sum:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # avoid duplication
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
