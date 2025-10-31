class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_to_freq = {}
        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 0
            num_to_freq[num] += 1

        return [num for num, freq in num_to_freq.items() if freq > 1]
