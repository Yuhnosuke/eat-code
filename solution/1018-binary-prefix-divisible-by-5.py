class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0

        for bit in nums:
            curr = (curr * 2 + bit) % 5
            ans.append(curr == 0)

        return ans
