class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_to_freq = {}
        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 0
            num_to_freq[num] += 1

        ans = 0
        for num, freq in num_to_freq.items():
            if num + 1 in num_to_freq:
                ans = max(ans, freq + num_to_freq[num + 1])

        return ans
