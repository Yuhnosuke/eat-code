class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_to_freq = Counter(t)
        window_counts = defaultdict(int)

        required = len(t_to_freq)
        formed = 0

        l = 0
        r = 0

        ans = (float("inf"), None, None)  # (window length, left, right)

        while r < len(s):
            ch = s[r]
            window_counts[ch] += 1

            if ch in t_to_freq and window_counts[ch] == t_to_freq[ch]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                left_char = s[l]
                window_counts[left_char] -= 1

                if (
                    left_char in t_to_freq
                    and window_counts[left_char] < t_to_freq[left_char]
                ):
                    formed -= 1

                l += 1

            r += 1

        if ans[0] == float("inf"):
            return ""
        return s[ans[1] : ans[2] + 1]
