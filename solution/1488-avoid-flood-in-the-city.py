from bisect import bisect_right


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        lake_to_last_rained_day_idx = {}  # lake -> last rained day index
        dry_days = []  # sroted list of indices where rains[i] == 0

        for i, rain in enumerate(rains):
            if rain == 0:
                ans[i] = 1
                p = bisect_right(dry_days, i)
                dry_days.insert(p, i)
            else:
                ans[i] == -1
                if rain in lake_to_last_rained_day_idx:
                    last_rained_day_idx = lake_to_last_rained_day_idx[rain]
                    p = bisect_right(dry_days, last_rained_day_idx)
                    if p == len(dry_days):
                        return []
                    dry_day = dry_days[p]
                    ans[dry_day] = rain
                    dry_days.pop(p)
                lake_to_last_rained_day_idx[rain] = i

        return ans
