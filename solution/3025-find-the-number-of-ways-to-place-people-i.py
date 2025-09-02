class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        N = len(points)

        for a in range(N):
            ax, ay = points[a]

            for b in range(N):
                if a == b:
                    continue

                bx, by = points[b]

                if ax <= bx and ay >= by:
                    blocked = False

                    for c in range(N):
                        if c == a or c == b:
                            continue

                        cx, cy = points[c]

                        if ax <= cx <= bx and ay >= cy >= by:
                            blocked = True
                            break

                    if not blocked:
                        ans += 1

        return ans
