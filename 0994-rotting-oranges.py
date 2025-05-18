from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        fresh_count = 0
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))

        ans = 0

        def is_inboundary(r, c):
            return 0 <= r < rows and 0 <= c < columns

        def is_fresh(r, c):
            return grid[r][c] == 1

        def is_visited(r, c):
            return (r, c) in visited

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            nodes_in_current_level = len(q)

            for _ in range(nodes_in_current_level):

                r, c, steps = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        is_inboundary(nr, nc)
                        and is_fresh(nr, nc)
                        and not is_visited(nr, nc)
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc, steps + 1))

                        fresh_count -= 1
                        ans = steps + 1

        return ans if fresh_count == 0 else -1
