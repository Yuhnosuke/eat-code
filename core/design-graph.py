class Graph:

    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []

        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False

        if dst not in self.graph:
            return False

        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()

        def dfs(src, dst):
            if src == dst:
                return True

            visited.add(src)

            for neighbor in self.graph.get(src, []):
                if neighbor not in visited:
                    if dfs(neighbor, dst):
                        return True

            visited.remove(src)

            return False

        return dfs(src, dst)
