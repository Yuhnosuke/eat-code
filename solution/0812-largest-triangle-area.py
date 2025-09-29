class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0

        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]

                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]

                    ans = max(
                        abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2, ans
                    )

        return ans
