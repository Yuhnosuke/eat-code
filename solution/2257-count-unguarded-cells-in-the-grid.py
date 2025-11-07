class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        rows, columns = m, n
        grid = [["."] * columns for _ in range(rows)]

        for gr, gc in guards:
            grid[gr][gc] = "G"
        for wr, wc in walls:
            grid[wr][wc] = "W"

        guarded_cells = set()

        def is_invalid(r, c):
            return r < 0 or r >= rows or c < 0 or c >= columns

        def is_obstructed(r, c):
            return grid[r][c] == "W" or grid[r][c] == "G"

        def dfs_north(r, c):
            if is_invalid(r, c) or is_obstructed(r, c):
                return

            guarded_cells.add((r, c))
            dfs_north(r - 1, c)
            return

        def dfs_east(r, c):
            if is_invalid(r, c) or is_obstructed(r, c):
                return

            guarded_cells.add((r, c))
            dfs_east(r, c + 1)
            return

        def dfs_west(r, c):
            if is_invalid(r, c) or is_obstructed(r, c):
                return

            guarded_cells.add((r, c))
            dfs_west(r, c - 1)
            return

        def dfs_south(r, c):
            if is_invalid(r, c) or is_obstructed(r, c):
                return

            guarded_cells.add((r, c))
            dfs_south(r + 1, c)
            return

        for gr, gc in guards:
            dfs_north(gr - 1, gc)
            dfs_east(gr, gc + 1)
            dfs_west(gr, gc - 1)
            dfs_south(gr + 1, gc)

        return rows * columns - len(guarded_cells) - len(walls) - len(guards)
