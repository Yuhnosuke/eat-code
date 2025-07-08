class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []

        index_a = len(a) - 1
        index_b = len(b) - 1

        while index_a >= 0 or index_b >= 0 or carry == 1:
            if index_a >= 0:
                carry += int(a[index_a])
                index_a -= 1
            if index_b >= 0:
                carry += int(b[index_b])
                index_b -= 1

            ans.append(str(carry % 2))
            carry = carry // 2

        reversed_ans = reversed(ans)
        return "".join(reversed_ans)
