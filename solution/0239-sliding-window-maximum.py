# Brute Force 1
# Time Limit Exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        curr_max_index = 0
        ans = []

        for r in range(len(nums)):
            if nums[r] > nums[curr_max_index]:
                curr_max_index = r

            if r - l + 1 == k:
                ans.append(nums[curr_max_index])

                if curr_max_index == l:
                    l += 1
                    curr_max_index = l
                    for i in range(l + 1, r + 1):
                        if nums[i] > nums[curr_max_index]:
                            curr_max_index = i
                else:
                    l += 1

        return ans


# Brute Force 2
# Time Limit Exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l + k - 1
        ans = []

        while r < len(nums):
            ans.append(max(nums[l : r + 1]))

            l += 1
            r += 1

        return ans


# Deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], window_size: int) -> List[int]:
        max_indices = deque()  # Deque to store indices of potential max elements
        max_values_in_windows = []  # Final result list to store max in each window

        for current_index in range(len(nums)):
            # Remove indices that are outside the current window
            if max_indices and max_indices[0] < current_index - window_size + 1:
                max_indices.popleft()

            # Remove indices whose corresponding values are less than the current value
            # because they cannot be the max if current value is larger
            while max_indices and nums[current_index] > nums[max_indices[-1]]:
                max_indices.pop()

            # Append the current index to the deque
            max_indices.append(current_index)

            # Once the window is fully formed, record the max value (at the front of the deque)
            if current_index >= window_size - 1:
                max_values_in_windows.append(nums[max_indices[0]])

        return max_values_in_windows
