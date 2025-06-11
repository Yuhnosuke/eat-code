class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        visited = set()

        rows = len(matrix)
        columns = len(matrix[0])
        directions = [
            # right
            [0, 1],
            # down
            [1, 0],
            # left
            [0, -1],
            # up
            [-1, 0],
        ]
        length = len(directions)

        # direction_index represents the current direction moving
        def dfs(r: int, c: int, direction_index: int) -> None:
            if len(visited) == rows * columns:
                return

            visited.add((r, c))
            ans.append(matrix[r][c])

            for i in range(length):
                new_direction_index = (direction_index + i) % length
                dr, dc = directions[new_direction_index]
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited:
                    dfs(nr, nc, new_direction_index)

        dfs(0, 0, 0)
        return ans
