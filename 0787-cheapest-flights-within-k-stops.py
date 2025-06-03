# Time Complexity: O(E * K * Log(N * K))
# Space Complexity: O(N * K *E)
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # src -> (dst, price)
        adj = {i: [] for i in range(n)}
        for u, v, price in flights:
            adj[u].append((v, price))

        min_heap = []
        # (price, src, k)
        for nei, p in adj[src]:
            heapq.heappush(min_heap, (p, nei, k - 1))

        visited = set()
        visited.add((src, k))

        ans = []

        while min_heap:
            curr_price, node, stops = heapq.heappop(min_heap)

            if node == dst:
                ans.append(curr_price)

            if stops < 0:
                continue

            if (node, stops) in visited:
                continue

            visited.add((node, stops))

            for nei_node, nei_price in adj[node]:
                heapq.heappush(min_heap, (curr_price + nei_price, nei_node, stops - 1))

        return min(ans) if ans else -1
