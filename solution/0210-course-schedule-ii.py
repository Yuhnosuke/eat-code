class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)
            visited.add(course)

            for prerequisite in adj[course]:
                if not dfs(prerequisite):
                    return False

            path.remove(course)
            topological_order.append(course)
            return True

        visited = set()
        path = set()
        topological_order = []

        for i in range(numCourses):
            if not dfs(i):
                return []

        return topological_order
