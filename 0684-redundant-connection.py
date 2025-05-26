class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
