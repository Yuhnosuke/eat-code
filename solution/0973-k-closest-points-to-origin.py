import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            max_heap.append((-distance, (x, y)))

        heapq.heapify(max_heap)

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [b for a, b in max_heap]
