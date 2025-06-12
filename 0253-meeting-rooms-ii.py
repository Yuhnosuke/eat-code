"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        ans = 0
        current_meetings = 0

        s, e = 0, 0

        while s < len(intervals):
            if start_times[s] < end_times[e]:
                current_meetings += 1
                s += 1
            else:
                current_meetings -= 1
                e += 1

            ans = max(ans, current_meetings)

        return ans
