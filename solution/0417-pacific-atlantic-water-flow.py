class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        result = []
        visited = set()

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        def is_pacific(r: int, c: int) -> bool:
            return r < rows and c == 0 or r == 0 and c < columns

        def is_atlantic(r: int, c: int) -> bool:
            return r < rows and c == columns - 1 or r == rows - 1 and c < columns

        def is_in_boundary(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < columns

        def is_visited(r: int, c: int) -> bool:
            return (r, c) in visited

        def can_flow_to_pacific(r: int, c: int) -> bool:
            if is_pacific(r, c):
                return True

            visited.add((r, c))

            for dy, dx in directions:
                ny, nx = r + dy, c + dx

                if (
                    is_in_boundary(ny, nx)
                    and not is_visited(ny, nx)
                    and heights[r][c] >= heights[ny][nx]
                ):
                    if can_flow_to_pacific(ny, nx):
                        visited.remove((r, c))
                        return True

            visited.remove((r, c))
            return False

        def can_flow_atlantic(r: int, c: int) -> bool:
            if is_atlantic(r, c):
                return True

            visited.add((r, c))

            for dy, dx in directions:
                ny, nx = r + dy, c + dx

                if (
                    is_in_boundary(ny, nx)
                    and not is_visited(ny, nx)
                    and heights[r][c] >= heights[ny][nx]
                ):
                    if can_flow_atlantic(ny, nx):
                        visited.remove((r, c))
                        return True

            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(columns):
                if can_flow_to_pacific(r, c) and can_flow_atlantic(r, c):
                    result.append([r, c])

        return result


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        reachables_to_pacific = set()
        reachables_to_atlantic = set()

        def is_validated(row: int, column: int) -> bool:
            return 0 <= row < rows and 0 <= column < columns

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def dfs(row: int, column: int, reachables: set(), previous_height: int) -> None:
            if (
                (row, column) in reachables
                or not is_validated(row, column)
                or heights[row][column] < previous_height
            ):
                return

            reachables.add((row, column))

            for dx, dy in directions:
                new_row, new_column = dy + row, dx + column
                dfs(new_row, new_column, reachables, heights[row][column])

        for column in range(columns):
            dfs(0, column, reachables_to_pacific, heights[0][column])
            dfs(rows - 1, column, reachables_to_atlantic, heights[rows - 1][column])

        for row in range(rows):
            dfs(row, 0, reachables_to_pacific, heights[row][0])
            dfs(row, columns - 1, reachables_to_atlantic, heights[row][columns - 1])

        answer = []
        for row in range(rows):
            for column in range(columns):
                if (row, column) in reachables_to_pacific and (
                    row,
                    column,
                ) in reachables_to_atlantic:
                    answer.append([row, column])

        return answer
