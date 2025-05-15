import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if y != x:
                y = y - x
                heapq.heappush(max_heap, -y)

        return 0 if len(max_heap) == 0 else -max_heap[0]
