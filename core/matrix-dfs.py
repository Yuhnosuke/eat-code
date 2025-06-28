class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def is_inboundary(r, c):
            return 0 <= r < rows and 0 <= c < columns

        def is_visited(r, c):
            return (r, c) in visited

        def is_rock(r, c):
            return grid[r][c] == 1

        def dfs(r, c):
            if not is_inboundary(r, c) or is_visited(r, c) or is_rock(r, c):
                return 0

            if r == rows - 1 and c == columns - 1:
                return 1

            visited.add((r, c))

            count = 0

            for dc, dr in directions:
                new_r, new_c = dr + r, dc + c
                count += dfs(new_r, new_c)

            visited.remove((r, c))

            return count

        return dfs(0, 0)
