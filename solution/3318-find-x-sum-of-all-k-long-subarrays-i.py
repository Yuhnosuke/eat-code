class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l = 0
        n = len(nums)
        ans = []
        num_to_freq = {}

        def calc_x_sum():
            items = [(num, freq) for num, freq in num_to_freq.items() if freq > 0]
            items.sort(key=lambda item: (item[1], item[0]), reverse=True)
            return sum([num * freq for num, freq in items[:x]])

        for r in range(n):
            if nums[r] not in num_to_freq:
                num_to_freq[nums[r]] = 0
            num_to_freq[nums[r]] += 1

            if r - l + 1 > k:
                num_to_freq[nums[l]] -= 1
                if num_to_freq[nums[l]] == 0:
                    del num_to_freq[nums[l]]
                l += 1

            if r - l + 1 == k:
                ans.append(calc_x_sum())

        return ans
