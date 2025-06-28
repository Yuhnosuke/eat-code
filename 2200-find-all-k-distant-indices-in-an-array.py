class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        N = len(nums)

        for i in range(N):
            for j in range(N):
                if nums[j] == key and abs(i - j) <= k:
                    ans.append(i)
                    break
        return ans
