class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

    def get_size(self, x):
        return self.size[self.find(x)]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)

        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 in num_set:
                uf.union(num - 1, num)

            if num + 1 in num_set:
                uf.union(num, num + 1)

        for num in num_set:
            res = max(res, uf.get_size(num))

        return res


# check num - 1 to be the start of consecutive sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        global_longest = 0

        for num in num_set:
            if num - 1 not in num_set:

                local_longest = 1

                while num + local_longest in num_set:
                    local_longest += 1

                global_longest = max(global_longest, local_longest)

        return global_longest
