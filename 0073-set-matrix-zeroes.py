# Time Complexity: O(m * n * (m + n))
# Space Complexity: O(m * n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        original_zero_coordinates = []

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    original_zero_coordinates.append((row, column))

        while original_zero_coordinates:
            zero_row, zero_column = original_zero_coordinates.pop()

            for row in range(rows):
                matrix[row][zero_column] = 0
            for column in range(columns):
                matrix[zero_row][column] = 0

        return matrix


# Time Complexity: O(m * n)
# Space Complexity: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        does_first_row_originally_have_zero = False
        does_first_column_originally_have_zero = False

        # check the first row has zero or not
        for c in range(columns):
            if matrix[0][c] == 0:
                does_first_row_originally_have_zero = True
                break

        # check the first column has zero or not
        for r in range(rows):
            if matrix[r][0] == 0:
                does_first_column_originally_have_zero = True
                break

        # take note in the first row and column
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # set rows to zero based on the note
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, columns):
                    matrix[r][c] = 0

        # set columns to zero based on the note
        for c in range(1, columns):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        # set the first row to zero if there are originally 0
        if does_first_row_originally_have_zero:
            for c in range(columns):
                matrix[0][c] = 0

        # set the first column to zero if there are originally 0
        if does_first_column_originally_have_zero:
            for r in range(rows):
                matrix[r][0] = 0

        return matrix
