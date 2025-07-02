class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr, s, e):
            if e - s + 1 <= 1:
                return arr

            m = (s + e) // 2

            merge_sort(arr, s, m)
            merge_sort(arr, m + 1, e)

            merge(arr, s, m, e)

            return arr

        def merge(arr, s, m, e):
            left = arr[s : m + 1]
            right = arr[m + 1 : e + 1]

            l = 0
            r = 0
            a = s

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[a] = left[l]
                    l += 1
                else:
                    arr[a] = right[r]
                    r += 1
                a += 1

            while l < len(left):
                arr[a] = left[l]
                l += 1
                a += 1
            while r < len(right):
                arr[a] = right[r]
                r += 1
                a += 1

        return merge_sort(nums, 0, len(nums) - 1)
