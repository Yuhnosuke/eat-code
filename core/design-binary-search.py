def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


def binary_search_left_boundary(nums, target):
    l, r = 0, len(nums)

    while l < r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m + 1

    return l


def binary_search_right_boundary(nums, target):
    l, r = 0, len(nums)

    while l < r:
        m = (l + r) // 2

        if nums[m] > target:
            r = m
        else:
            l = m + 1

    return l
