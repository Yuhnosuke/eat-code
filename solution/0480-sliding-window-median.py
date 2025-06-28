import heapq
from collections import defaultdict


# two heap with lazy deletion
class MedianFinder:

    def __init__(self):
        self.smallers = []  # max_heap
        self.largers = []  # min_heap
        heapq.heapify(self.smallers)
        heapq.heapify(self.largers)

        self.nums_to_remove_lazily = defaultdict(int)
        # the size difference between the two heaps
        # negative: smallers heap has more
        # positive: largeer heap has more
        self.balance = 0

    def add(self, num):
        if not self.smallers or num <= -self.smallers[0]:
            heapq.heappush(self.smallers, -num)
            self.balance -= 1
        else:
            heapq.heappush(self.largers, num)
            self.balance += 1

        self.rebalance()

    def remove(self, num):
        self.nums_to_remove_lazily[num] += 1

        if num <= -self.smallers[0]:
            self.balance += 1
        else:
            self.balance -= 1

        self.rebalance()
        self.lazy_remove()

    def find_median(self):
        if self.balance < 0:
            return -self.smallers[0]
        if self.balance > 0:
            return self.largers[0]
        return (-self.smallers[0] + self.largers[0]) / 2

    def rebalance(self):
        # when smallers is longer
        while self.balance < 0:
            heapq.heappush(self.largers, -heapq.heappop(self.smallers))
            self.balance += 2

        # when largers is longer
        while self.balance > 0:
            heapq.heappush(self.smallers, -heapq.heappop(self.largers))
            self.balance -= 2

    def lazy_remove(self):
        while self.smallers and self.nums_to_remove_lazily[-self.smallers[0]] > 0:
            self.nums_to_remove_lazily[-self.smallers[0]] -= 1
            heapq.heappop(self.smallers)

        while self.largers and self.nums_to_remove_lazily[self.largers[0]] > 0:
            self.nums_to_remove_lazily[self.largers[0]] -= 1
            heapq.heappop(self.largers)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []

        median_finder = MedianFinder()

        l = 0
        for r in range(len(nums)):
            median_finder.add(nums[r])

            if r - l + 1 > k:
                median_finder.remove(nums[l])
                l += 1

            if r - l + 1 == k:
                ans.append(median_finder.find_median())

        return ans


# brute force
# time limit exceeded
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        smallers = []  # max_heap
        largers = []  # min_heap

        heapq.heapify(smallers)
        heapq.heapify(largers)

        l = 0
        ans = []

        for r in range(len(nums)):

            if r - l + 1 > k:
                if -1 * nums[l] in smallers:
                    smallers.remove(-1 * nums[l])
                    heapq.heapify(smallers)
                elif nums[l] in largers:
                    largers.remove(nums[l])
                    heapq.heapify(largers)

                l += 1

            heapq.heappush(smallers, -1 * nums[r])

            if len(smallers) > 0 and len(largers) > 0 and -1 * smallers[0] > largers[0]:
                largest_in_smallers = -1 * heapq.heappop(smallers)
                heapq.heappush(largers, largest_in_smallers)

            if len(smallers) > len(largers) + 1:
                largest_in_smallers = -1 * heapq.heappop(smallers)
                heapq.heappush(largers, largest_in_smallers)

            if len(largers) > len(smallers) + 1:
                smallest_in_largers = heapq.heappop(largers)
                heapq.heappush(smallers, -1 * smallest_in_largers)

            if r - l + 1 == k:
                if len(smallers) > len(largers):
                    ans.append(-1 * smallers[0])
                elif len(largers) > len(smallers):
                    ans.append(largers[0])
                else:
                    ans.append((-1 * smallers[0] + largers[0]) / 2)
        return ans
