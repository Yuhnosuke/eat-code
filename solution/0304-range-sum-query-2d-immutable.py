from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])

        self.prefix = []

        for r in range(rows):
            curr_row = [0]
            for c in range(columns):
                curr_row.append(curr_row[-1] + matrix[r][c])
            self.prefix.append(curr_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.prefix[r][col2 + 1] - self.prefix[r][col1]

        return total


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])

        self.prefix = [[0] * (columns + 1)]

        for r in range(rows):
            curr_row = [0]

            for c in range(columns):
                curr_row.append(curr_row[-1] + matrix[r][c])

            for i in range(len(curr_row)):
                curr_row[i] += self.prefix[r][i]
            self.prefix.append(curr_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_left = self.prefix[row2][col2]
        top = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        duplicated = self.prefix[row1 - 1][col1 - 1]

        return bottom_left - top - left + duplicated


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
