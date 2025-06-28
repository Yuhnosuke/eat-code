class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        rotated = [None] * N

        for i in range(N):
            rotated[(i + k) % N] = nums[i]

        for i in range(N):
            nums[i] = rotated[i]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        origin_before = nums[:-k]
        origin_after = nums[-k:]

        for i in range(len(origin_after)):
            nums[i] = origin_after[i]

        for i in range(len(origin_before)):
            nums[k + i] = origin_before[i]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k != 0:

            origin_before = nums[:-k]
            origin_after = nums[-k:]

            nums[:k], nums[k:] = origin_after, origin_before


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]

                l += 1
                r -= 1

        if k != 0:
            reverse(nums, 0, len(nums) - 1)
            reverse(nums, 0, k - 1)
            reverse(nums, k, len(nums) - 1)
