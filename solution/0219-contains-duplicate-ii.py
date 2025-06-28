class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l = 0
        nums_in_current_window = set()
        nums_in_current_window.add(nums[0])

        for r in range(l + 1, len(nums)):
            if r - l > k:
                nums_in_current_window.remove(nums[l])
                l += 1

            if nums[r] in nums_in_current_window:
                return True

            nums_in_current_window.add(nums[r])

        return False
