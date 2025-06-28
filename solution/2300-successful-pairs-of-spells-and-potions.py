# Time Coplexity: O(m * log m + n * log m)
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:

        def binary_search(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)

            while l < r:
                m = (l + r) // 2

                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1

            return l

        potions.sort()
        ans = []

        for spell in spells:
            threshold = success / spell
            l = binary_search(potions, threshold)
            ans.append(len(potions) - l)

        return ans


# Time Coplexity: O(n ** m) (Time Limit Exceeded)
class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ans = []

        for spell in spells:
            threshold = success / spell
            ans.append(len(list(filter(lambda x: x >= threshold, potions))))

        return ans
