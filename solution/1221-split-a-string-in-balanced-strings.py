class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ch_to_freq = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(s)):
            ch_to_freq[s[r]] += 1

            if ch_to_freq["L"] == ch_to_freq["R"]:
                ans += 1

                ch_to_freq["L"] = 0
                ch_to_freq["R"] = 0

                l = r + 1
                r = r + 1

        return ans


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, count = 0, 0

        for ch in s:
            if ch == "L":
                count -= 1
            else:
                count += 1

            if count == 0:
                ans += 1

        return ans
