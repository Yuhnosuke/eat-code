class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums

        if a + b <= c:
            return "none"

        side_to_freq = {}

        for num in nums:
            if num not in side_to_freq:
                side_to_freq[num] = 0
            side_to_freq[num] += 1

        if len(side_to_freq) == 1:
            return "equilateral"
        if len(side_to_freq) == 2:
            return "isosceles"
        return "scalene"
