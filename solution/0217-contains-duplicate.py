class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        return not all([value == 1 for value in freq.values()])
