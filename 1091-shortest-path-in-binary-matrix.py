from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        visited.add((0, 0))

        q = deque()
        q.append((0, 0, 1))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        def is_inboundary(r, c):
            return 0 <= r < rows and 0 <= c < columns

        def is_visited(r, c):
            return (r, c) in visited

        def is_zero(r, c):
            return grid[r][c] == 0

        while q:
            nodes_in_current_level = len(q)

            for _ in range(nodes_in_current_level):

                r, c, steps = q.popleft()

                if r == rows - 1 and c == columns - 1:
                    return steps

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        is_inboundary(nr, nc)
                        and not is_visited(nr, nc)
                        and is_zero(nr, nc)
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc, steps + 1))

        return -1
