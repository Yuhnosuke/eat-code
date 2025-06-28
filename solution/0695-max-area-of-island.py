class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        ans = 0

        def is_land(r, c):
            return grid[r][c] == 1

        def is_visited(r, c):
            return (r, c) in visited

        def is_inboundary(r, c):
            return 0 <= r < rows and 0 <= c < columns

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        def dfs(r, c):
            if not is_inboundary(r, c) or is_visited(r, c) or not is_land(r, c):
                return 0

            visited.add((r, c))

            areas = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                areas += dfs(nr, nc)

            return areas

        for r in range(rows):
            for c in range(columns):
                if is_land(r, c) and not is_visited(r, c):
                    ans = max(ans, dfs(r, c))

        return ans
