class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = {i: [] for i in range(n)}

        # a -> [(b, p)]
        # b -> [(a, p)]
        for [a, b], p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        visited = set()

        # (proba, node)
        max_heap = [(-1, start_node)]
        heapq.heapify(max_heap)

        while max_heap:
            curr_prob, curr_node = heapq.heappop(max_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            if curr_node == end_node:
                return -curr_prob

            for nei_node, nei_prob in graph[curr_node]:
                if nei_node not in visited:
                    heapq.heappush(max_heap, (curr_prob * nei_prob, nei_node))

        return 0
