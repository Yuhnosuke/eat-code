class Spreadsheet:

    def __init__(self, rows: int):
        self.column_labels = [chr(code) for code in range(ord("A"), ord("A") + 26)]
        self.hash_map = {}

        for r in range(rows):
            for c in self.column_labels:
                self.hash_map[(r, c)] = 0

    def setCell(self, cell: str, value: int) -> None:
        r = int(cell[1:])
        c = cell[0]

        self.hash_map[(r - 1, c)] = value

    def resetCell(self, cell: str) -> None:
        r = int(cell[1:])
        c = cell[0]
        self.hash_map[(r - 1, c)] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        splited = formula.split("+")

        a, b = splited

        if a[0] in self.column_labels:
            a = self.hash_map[(int(a[1:]) - 1, a[0])]

        if b[0] in self.column_labels:
            b = self.hash_map[(int(b[1:]) - 1, b[0])]

        return int(a) + int(b)


class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.grid = [[0] * 26 for _ in range(rows)]

    @staticmethod
    def _parse_cell(cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord("A")  # 0..25
        row = int(cell[1:]) - 1  # 0-index
        return row, col

    @staticmethod
    def _token_value(token: str, grid: list[list[int]]) -> int:
        if token[0].isdigit():
            return int(token)

        col = ord(token[0]) - ord("A")
        row = int(token[1:]) - 1

        return grid[row][col]

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parse_cell(cell)
        self.grid[r][c] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+", 1)
        return self._token_value(x, self.grid) + self._token_value(y, self.grid)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
