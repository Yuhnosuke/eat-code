class UnionFind:

    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_of_components = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1

        self.num_of_components -= 1

        return True

    def getNumComponents(self) -> int:
        return self.num_of_components
