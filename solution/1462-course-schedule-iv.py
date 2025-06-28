class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for pre, course in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # 各ノードについて、そのすべての前提を記録する集合
        prereq_set = [set() for _ in range(numCourses)]

        # トポロジカル順序で処理するためのキュー
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            current = queue.popleft()

            for neighbor in adj[current]:
                # neighbor の前提に current を加える
                prereq_set[neighbor].add(current)
                # neighbor の前提に current の前提も加える（伝播）
                prereq_set[neighbor].update(prereq_set[current])

                # neighborの依存関係が1つ解消
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        res = []
        for u, v in queries:
            res.append(u in prereq_set[v])
        return res
