class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid)

        def sort_in_non_increasing(r, c):
            nums = []
            origin_r = r
            origin_c = c

            while r < rows:
                nums.append(grid[r][c])
                r += 1
                c += 1
            nums.sort(reverse=True)

            i = 0
            while origin_r < rows:
                grid[origin_r][origin_c] = nums[i]
                origin_r += 1
                origin_c += 1
                i += 1

        def sort_in_non_decreasing(r, c):
            nums = []
            origin_r = r
            origin_c = c

            while c < columns:
                nums.append(grid[r][c])
                r += 1
                c += 1
            nums.sort()

            i = 0
            while origin_c < columns:
                grid[origin_r][origin_c] = nums[i]
                origin_r += 1
                origin_c += 1
                i += 1

        for r in range(rows):
            sort_in_non_increasing(r, 0)

        for c in range(1, columns):
            sort_in_non_decreasing(0, c)

        return grid
