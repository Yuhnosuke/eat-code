# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge_sort_helper(array, s, e):
            if e - s + 1 <= 1:
                return array

            m = (s + e) // 2

            merge_sort_helper(array, s, m)

            merge_sort_helper(array, m + 1, e)

            merge_helper(array, s, m, e)

            return array

        def merge_helper(array, s, m, e):

            left = array[s : m + 1]
            right = array[m + 1 : e + 1]

            i = s
            l = 0
            r = 0

            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    array[i] = left[l]
                    l += 1
                else:
                    array[i] = right[r]
                    r += 1
                i += 1

            while l < len(left):
                array[i] = left[l]
                l += 1
                i += 1
            while r < len(right):
                array[i] = right[r]
                r += 1
                i += 1

        return merge_sort_helper(pairs, 0, len(pairs) - 1)
