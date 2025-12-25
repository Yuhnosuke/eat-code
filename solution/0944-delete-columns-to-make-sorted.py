class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        columns = len(strs[0])

        ans = 0

        for c in range(columns):
            for r in range(1, rows):
                prev, curr = strs[r - 1][c], strs[r][c]
                if prev > curr:
                    ans += 1
                    break

        return ans
