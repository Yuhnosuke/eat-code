class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []

        # src -> (dst, weight)
        for u, v, w in times:
            graph[u].append((v, w))

        visited = set()
        time_elasped = 0

        # (time, node)
        min_heap = [(0, k)]

        while min_heap:

            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)
            time_elasped = curr_time

            for nei_node, nei_time in graph[curr_node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (curr_time + nei_time, nei_node))

        return time_elasped if len(visited) == n else -1
