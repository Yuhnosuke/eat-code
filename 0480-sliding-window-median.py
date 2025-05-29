import heapq


# TODO: Lazy Deletion
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
