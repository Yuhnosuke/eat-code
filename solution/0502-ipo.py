import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:

        max_profit_heap = []
        min_capital_heap = []

        for c, p in zip(capital, profits):
            min_capital_heap.append((c, p))

        heapq.heapify(max_profit_heap)
        heapq.heapify(min_capital_heap)

        curr_capital = w

        for _ in range(k):
            while min_capital_heap and min_capital_heap[0][0] <= curr_capital:
                c, p = heapq.heappop(min_capital_heap)

                heapq.heappush(max_profit_heap, -p)

            # no more project is available because of short of capital
            if not max_profit_heap:
                break

            curr_capital += -heapq.heappop(max_profit_heap)

        return curr_capital
