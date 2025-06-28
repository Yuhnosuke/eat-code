class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rows = len(matrix)
        columns = len(matrix[0])

        rotated = [[0] * len(matrix) for _ in range(len(matrix))]

        for row in range(rows):
            for column in range(columns):
                rotated[column][n - 1 - row] = matrix[row][column]

        for row in range(rows):
            for column in range(columns):
                matrix[row][column] = rotated[row][column]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        # 1. swap vertically
        top = 0
        bottom = rows - 1

        while top < bottom:
            for column in range(columns):
                tmp = matrix[top][column]

                matrix[top][column] = matrix[bottom][column]
                matrix[bottom][column] = tmp

            top += 1
            bottom -= 1

        # 2. swap diagonally
        for row in range(rows):
            # start from rows + 1 to prevent from swapping twice
            for column in range(row + 1, columns):
                tmp = matrix[row][column]

                matrix[row][column] = matrix[column][row]
                matrix[column][row] = tmp

        return matrix
