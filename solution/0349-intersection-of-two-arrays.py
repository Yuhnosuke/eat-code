class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1, p2 = 0, 0
        ans = set()

        nums1.sort()
        nums2.sort()

        while p1 < len(nums1) and p2 < len(nums2):
            num1, num2 = nums1[p1], nums2[p2]

            if num1 == num2:
                ans.add(num1)
                p1 += 1
                p2 += 1
            elif num1 < num2:
                p1 += 1
            else:
                p2 += 1

        return list(ans)
