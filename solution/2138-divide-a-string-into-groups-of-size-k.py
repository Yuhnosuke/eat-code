class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        length = len(s)
        curr = 0
        while curr < length:
            ans.append(s[curr : curr + k])
            curr += k

        ans[-1] += fill * (k - len(ans[-1]))
        return ans
