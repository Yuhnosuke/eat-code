class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pairs = [(i, nums[i]) for i in range(len(nums))]
        pairs.sort(key=lambda x: -x[1])

        k_pairs = pairs[:k]
        k_pairs.sort()

        return list(map(lambda x: x[1], k_pairs))
