class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return sorted(
            map(lambda d: [math.sqrt(d[0] ** 2 + d[1] ** 2), d[0] * d[1]], dimensions)
        )[len(dimensions) - 1][1]
