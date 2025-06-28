class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        f = 0
        s = 0

        while True:
            f = nums[nums[f]]
            s = nums[s]

            if f == s:
                break

        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

            if s == s2:
                return s
