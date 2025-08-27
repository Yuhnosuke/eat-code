class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        ans = 0

        def is_in_boundary(r, c):
            return r >= 0 and r < rows and c >= 0 and c < columns

        @lru_cache(None)
        def dfs(r: int, c: int, direction: int, can_turn: bool, next_num: int) -> int:
            dx, dy = directions[direction][0], directions[direction][1]
            nc, nr = c + dx, r + dy

            if not is_in_boundary(nr, nc) or grid[nr][nc] != next_num:
                return 0

            max_length = dfs(nr, nc, direction, can_turn, 2 - next_num)

            if can_turn:
                max_length = max(
                    max_length,
                    dfs(nr, nc, (direction + 1) % len(directions), False, 2 - next_num),
                )

            return max_length + 1

        directions = [
            [1, -1],  # 'bl_tr',
            [1, 1],  # 'tl_br',
            [-1, 1],  # 'tr_bl',
            [-1, -1],  # 'br_tl',
        ]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    for direction in range(len(directions)):
                        ans = max(ans, 1 + dfs(r, c, direction, True, 2))

        return ans
