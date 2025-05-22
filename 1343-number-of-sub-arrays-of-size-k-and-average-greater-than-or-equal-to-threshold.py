class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        curr_sum = 0

        l = 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                curr_sum -= arr[l]
                l += 1

            curr_sum += arr[r]

            if r - l + 1 == k and curr_sum / k >= threshold:
                ans += 1

        return ans
