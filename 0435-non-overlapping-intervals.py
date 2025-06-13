class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        ans = 0

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            # overlap
            if curr_start < prev_end:
                ans += 1
                prev_end = min(prev_end, curr_end)
            # not overlap
            else:
                prev_end = curr_end

        return ans
