# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quick_sort_helper(array, s, e):
            if e - s + 1 <= 1:
                return array

            # partition
            pivot = array[e]
            left = s

            for i in range(s, e):
                if array[i].key < pivot.key:
                    tmp = array[left]
                    array[left] = array[i]
                    array[i] = tmp

                    left += 1

            # swap left and e
            tmp = array[left]
            array[left] = array[e]
            array[e] = tmp

            # quick sort left subarray
            quick_sort_helper(array, s, left - 1)

            # quick sort right subarray
            quick_sort_helper(array, left + 1, e)

            # return array
            return array

        return quick_sort_helper(pairs, 0, len(pairs) - 1)
