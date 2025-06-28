class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        past_day_stack = []
        ans = [0] * len(temperatures)

        for curr_day in range(len(temperatures)):
            curr_temp = temperatures[curr_day]

            while past_day_stack and curr_temp > temperatures[past_day_stack[-1]]:
                past_day = past_day_stack.pop()
                ans[past_day] = curr_day - past_day

            past_day_stack.append(curr_day)

        return ans
