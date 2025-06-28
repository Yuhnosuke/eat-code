class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list
        # src -> (dst, weight)
        adj = {i: [] for i in range(n)}
        for src, dst, weight in edges:
            adj[src].append((dst, weight))
            adj[dst].append((src, weight))

        # initialize min heap
        # (weight, src, dst)
        min_heap = []
        start_node = edges[0][0]
        for neighbor, weight in adj[start_node]:
            heapq.heappush(min_heap, (weight, start_node, neighbor))

        # initialize visited set
        visited = set()
        visited.add(start_node)

        # minimum spanning tree
        # (src, dst, weight)
        mst = []

        # prim
        while min_heap:
            weight, src, dst = heapq.heappop(min_heap)

            if dst in visited:
                continue

            visited.add(dst)
            mst.append((src, dst, weight))

            for nei_node, nei_weight in adj[dst]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_weight, dst, nei_node))

        # calc total weight
        if len(visited) != n:
            return -1

        min_weight = 0
        for src, dst, weight in mst:
            min_weight += weight
        return min_weight
