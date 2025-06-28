import heapq


class MedianFinder:

    def __init__(self):
        self.smallers = []  # max_heap
        self.largers = []  # min_heap

        heapq.heapify(self.smallers)
        heapq.heapify(self.largers)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallers, -1 * num)

        if (
            len(self.smallers) > 0
            and len(self.largers) > 0
            and -1 * self.smallers[0] > self.largers[0]
        ):
            largest_num_in_smallers = -1 * heapq.heappop(self.smallers)
            heapq.heappush(self.largers, largest_num_in_smallers)

        if len(self.smallers) > len(self.largers) + 1:
            largest_num_in_smallers = -1 * heapq.heappop(self.smallers)
            heapq.heappush(self.largers, largest_num_in_smallers)

        if len(self.largers) > len(self.smallers) + 1:
            smallest_num_in_largers = heapq.heappop(self.largers)
            heapq.heappush(self.smallers, -1 * smallest_num_in_largers)

    def findMedian(self) -> float:
        if len(self.smallers) > len(self.largers):
            return -1 * self.smallers[0]

        if len(self.largers) > len(self.smallers):
            return self.largers[0]

        return (-1 * self.smallers[0] + self.largers[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
