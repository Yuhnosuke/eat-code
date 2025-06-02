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
