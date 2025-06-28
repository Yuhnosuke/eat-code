class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str_max, num_str_min = str(num), str(num)
        p = 0

        while p < len(num_str_max) and num_str_max[p] == "9":
            p += 1

        if p < len(num_str_max):
            num_str_max = num_str_max.replace(num_str_max[p], "9")

        num_str_min = num_str_min.replace(num_str_min[0], "0")

        num_max, num_min = int(num_str_max), int(num_str_min)

        return num_max - num_min
