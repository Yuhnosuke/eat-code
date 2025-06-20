# Brute Force
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        l = 0
        r = len(merged) - 1

        if len(merged) % 2:
            m = (l + r) // 2
            return merged[m]

        lm = (l + r) // 2
        rm = ceil((l + r) / 2)
        return (merged[lm] + merged[rm]) / 2


# Binary Search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp

        l = 0
        r = len(nums1)

        while True:
            partition1 = (l + r) // 2
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            min_right1 = nums1[partition1] if partition1 < len(nums1) else float("inf")
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            min_right2 = nums2[partition2] if partition2 < len(nums2) else float("inf")

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (len(nums1) + len(nums2)) % 2:
                    return max(max_left1, max_left2)
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                r = partition1 - 1
            elif max_left2 > min_right1:
                l = partition1 + 1
