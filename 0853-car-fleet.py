class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet_stack = []
        car_locations = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(car_locations, reverse=True):
            time_to_target = (target - p) / s

            if not car_fleet_stack or time_to_target > car_fleet_stack[-1]:
                car_fleet_stack.append(time_to_target)

        return len(car_fleet_stack)
