class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        max_heap = []

        for p, t in classes:
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        total = 0
        for _, p, t in max_heap:
            total += p / t

        return total / len(classes)
