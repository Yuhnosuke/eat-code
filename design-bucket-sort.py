from typing import List


def bucket_sort(array: List[int]):
    counts = [0, 0, 0]

    for i in range(len(array)):
        counts[array[i]] += 1

    # pointer for the position of insertion to array
    i = 0

    # pointer for the array of frequency of numbers
    for c in range(len(counts)):
        # insert actual number as long as it appeared to array
        for _ in range(counts[c]):
            array[i] = c
            i += 1

    return array
