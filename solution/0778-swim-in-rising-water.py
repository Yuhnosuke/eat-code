class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # (time, row, column)
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()
        visited.add((0, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:

            time, row, column = heapq.heappop(min_heap)

            if row == n - 1 and column == n - 1:
                return time

            for dr, dc in directions:
                nei_r, nei_c = row + dr, column + dc

                if (
                    nei_r < 0
                    or nei_c < 0
                    or nei_r == n
                    or nei_c == n
                    or (nei_r, nei_c) in visited
                ):
                    continue

                visited.add((nei_r, nei_c))
                heapq.heappush(min_heap, (max(time, grid[nei_r][nei_c]), nei_r, nei_c))
