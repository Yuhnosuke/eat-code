class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        positive_diagnals = set()
        negative_diagnals = set()

        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copied = ["".join(row) for row in board]
                ans.append(copied)
                return

            for c in range(n):
                if (
                    c in columns
                    or (r + c) in positive_diagnals
                    or (r - c) in negative_diagnals
                ):
                    continue

                columns.add(c)
                positive_diagnals.add(r + c)
                negative_diagnals.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                columns.remove(c)
                positive_diagnals.remove(r + c)
                negative_diagnals.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return ans
