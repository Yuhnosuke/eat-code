class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l = 0
        n = len(nums)
        ans = []
        num_to_freq = {}

        def calc_x_sum():
            return sum(
                map(
                    lambda x: x[0] * x[1],
                    sorted(
                        [(num, freq) for num, freq in num_to_freq.items()],
                        key=lambda x: (x[1], x[0]),
                        reverse=True,
                    )[:x],
                )
            )

        for r in range(n):
            if nums[r] not in num_to_freq:
                num_to_freq[nums[r]] = 0
            num_to_freq[nums[r]] += 1

            if r - l + 1 > k:
                if num_to_freq[nums[l]] == 0:
                    del num_to_freq[nums[l]]
                else:
                    num_to_freq[nums[l]] -= 1
                l += 1

            if r - l + 1 == k:
                x_sum = calc_x_sum()
                ans.append(x_sum)

        return ans
