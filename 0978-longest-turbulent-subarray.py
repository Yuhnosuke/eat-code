class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        max_len = 1
        increasing_len = 1
        decreasing_len = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                increasing_len = decreasing_len + 1
                decreasing_len = 1
            elif arr[i] < arr[i - 1]:
                decreasing_len = increasing_len + 1
                increasing_len = 1
            else:
                increasing_len = 1
                decreasing_len = 1

            max_len = max(max_len, increasing_len, decreasing_len)

        return max_len
