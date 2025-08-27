class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        start = nums[0]
        prev = nums[0]

        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                ans.append(f"{start}->{prev}" if start != prev else str(start))
                start = num
                prev = num

        ans.append(f"{start}->{prev}" if start != prev else str(start))
        return ans
