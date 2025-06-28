# Prim's 1
# this is not efficient because each node is stored as set,
# which uses extra memory.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # build adjacency list
        # src -> (dst, cost)
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]

            for j in range(i + 1, len(points)):
                xj, yj = points[j]

                distance = abs(xi - xj) + abs(yi - yj)

                adj[(xi, yi)].append(((xj, yj), distance))
                adj[(xj, yj)].append(((xi, yi), distance))

        # inilialize min_heap
        # (cost, src, dst)
        min_heap = []
        start_point = points[0]
        for dst, cost in adj[(start_point[0], start_point[1])]:
            heapq.heappush(
                min_heap, (cost, (start_point[0], start_point[1]), (dst[0], dst[1]))
            )

        # initialize visited set
        visited = set()
        visited.add((start_point[0], start_point[1]))

        # minimum spanning tree
        # (src, dst, cost)
        mst = []

        # prim
        while len(visited) < len(points):
            cost, src, dst = heapq.heappop(min_heap)

            if (dst[0], dst[1]) in visited:
                continue

            visited.add((dst[0], dst[1]))

            mst.append(
                (
                    (src[0], src[1]),
                    (dst[0], dst[1]),
                    cost,
                )
            )

            for nei_node, nei_cost in adj[(dst[0], dst[1])]:
                if (nei_node[0], nei_node[1]) not in visited:
                    heapq.heappush(
                        min_heap,
                        (
                            nei_cost,
                            (dst[0], dst[1]),
                            (nei_node[0], nei_node[1]),
                        ),
                    )

        min_cost = 0
        for src, dst, cost in mst:
            min_cost += cost
        return min_cost


# Prim's 2
# node should be denoted as index(int).
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # build adjacency list
        # src -> (dst, cost)
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]

            for j in range(i + 1, len(points)):
                xj, yj = points[j]

                distance = abs(xi - xj) + abs(yi - yj)

                adj[i].append((j, distance))
                adj[j].append((i, distance))

        # inilialize min_heap
        # (cost, node)
        min_heap = [(0, 0)]

        # initialize visited set
        visited = set()

        min_cost = 0

        # prim
        while len(visited) < len(points):
            cost, dst = heapq.heappop(min_heap)

            if dst in visited:
                continue

            visited.add(dst)

            min_cost += cost

            for nei_node, nei_cost in adj[dst]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei_node))

        return min_cost


# Kruskal's
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.connected_components = n

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
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        self.connected_components -= 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # (cost, v1, v2)
        min_heap = []
        for i in range(len(points)):
            xi, yi = points[i]

            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (dist, i, j))

        min_cost = 0
        uf = UnionFind(len(points))

        while uf.connected_components > 1:
            cost, i, j = heapq.heappop(min_heap)

            if not uf.union(i, j):
                continue

            min_cost += cost

        return min_cost
