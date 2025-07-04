class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for row in range(1, numRows):
            length = row + 1
            curr_row = [0] * length
            curr_row[0] = 1
            curr_row[length - 1] = 1

            if row == 1:
                ans.append(curr_row)
            else:
                for i in range(1, len(curr_row) - 1):
                    curr_row[i] = ans[row - 1][i - 1] + ans[row - 1][i]
                ans.append(curr_row)

        return ans
