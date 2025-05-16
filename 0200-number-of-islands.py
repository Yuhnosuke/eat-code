class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        ans = 0

        def is_inboundary(r, c):
            return 0 <= r < rows and 0 <= c < columns

        def is_visited(r, c):
            return (r, c) in visited

        def is_land(r, c):
            return grid[r][c] == "1"

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        def dfs(r, c):

            for dc, dr in directions:
                nr, nc = dr + r, dc + c

                if is_inboundary(nr, nc) and not is_visited(nr, nc) and is_land(nr, nc):
                    visited.add((nr, nc))
                    dfs(nr, nc)

            return 1

        for r in range(rows):
            for c in range(columns):
                if not is_visited(r, c) and is_land(r, c):
                    visited.add((r, c))
                    ans += dfs(r, c)

        return ans
