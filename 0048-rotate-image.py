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
