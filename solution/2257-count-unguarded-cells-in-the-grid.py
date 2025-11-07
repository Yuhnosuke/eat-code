class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [["."] * n for _ in range(m)]
        guarded_cells = set()

        for guard, wall in zip_longest(guards, walls):
            if guard:
                grid[guard[0]][guard[1]] = "G"
            if wall:
                grid[wall[0]][wall[1]] = "W"

        def is_invalid(r, c):
            return r < 0 or r >= m or c < 0 or c >= n

        def is_obstructed(r, c):
            return grid[r][c] == "W" or grid[r][c] == "G"

        def dfs(r, c, direction):
            if is_invalid(r, c) or is_obstructed(r, c):
                return

            guarded_cells.add((r, c))

            if direction == "north":
                dfs(r - 1, c, "north")
            if direction == "east":
                dfs(r, c + 1, "east")
            if direction == "west":
                dfs(r, c - 1, "west")
            if direction == "south":
                dfs(r + 1, c, "south")

            return

        for gr, gc in guards:
            dfs(gr - 1, gc, "north")
            dfs(gr, gc + 1, "east")
            dfs(gr, gc - 1, "west")
            dfs(gr + 1, gc, "south")

        return m * n - len(guarded_cells) - len(walls) - len(guards)
