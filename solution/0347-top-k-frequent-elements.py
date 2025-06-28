class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1

        min_heap = []

        for num, freq in num_to_freq.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return list(map(lambda x: x[1], min_heap))


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1

        max_heap = []

        for num, freq in num_to_freq.items():
            heapq.heappush(max_heap, (-freq, num))

        while k > 0:
            freq, num = heapq.heappop(max_heap)
            res.append(num)
            k -= 1

        return res
