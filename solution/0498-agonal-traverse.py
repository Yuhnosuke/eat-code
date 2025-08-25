class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        columns = len(mat[0])

        is_right_up = True
        ans = []

        def is_in_boundary(r, c):
            return r >= 0 and r < rows and c >= 0 and c < columns

        def dfs(r, c):
            nonlocal is_right_up

            ans.append(mat[r][c])

            if r == rows - 1 and c == columns - 1:
                return

            if is_right_up:
                if is_in_boundary(r - 1, c + 1):
                    dfs(r - 1, c + 1)
                else:
                    is_right_up = False
                    if c + 1 < columns:
                        dfs(r, c + 1)
                    else:
                        dfs(r + 1, c)
            else:
                if is_in_boundary(r + 1, c - 1):
                    dfs(r + 1, c - 1)
                else:
                    is_right_up = True
                    if r + 1 < rows:
                        dfs(r + 1, c)
                    else:
                        dfs(r, c + 1)

        dfs(0, 0)
        return ans
