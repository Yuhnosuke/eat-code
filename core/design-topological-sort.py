class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)

        visited = set()
        path = set()
        topological_order = []

        # post order dfs
        # return True if not cycle
        # return False if cycle
        def dfs(src):
            if src in path:
                return False

            if src in visited:
                return True

            path.add(src)
            visited.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False

            topological_order.append(src)
            path.remove(src)
            return True

        for i in range(n):
            # if cycle detected
            if not dfs(i):
                return []

        topological_order.reverse()
        return topological_order
