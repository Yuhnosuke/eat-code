# dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prerequisite_graph = {}
        for c in range(numCourses):
            course_prerequisite_graph[c] = []

        for crs, pre in prerequisites:
            course_prerequisite_graph[crs].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if course_prerequisite_graph[course] == []:
                return True

            visited.add(course)

            for prerequisite in course_prerequisite_graph[course]:
                if not dfs(prerequisite):
                    return False

            visited.remove(course)
            course_prerequisite_graph[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


# topological sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        visited = set()
        path = set()
        # topological_order = []

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

            # topological_order.append(course)
            path.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
