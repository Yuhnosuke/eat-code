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
