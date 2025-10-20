class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        past_days = []
        ans = [0] * len(temperatures)

        for t in range(len(temperatures)):
            while past_days and temperatures[past_days[-1]] < temperatures[t]:
                p = past_days.pop()
                ans[p] = t - p
            past_days.append(t)
        return ans
