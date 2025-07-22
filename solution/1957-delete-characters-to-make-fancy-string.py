# O(n ** 2)
# Time Limit Exceeded
class Solution:
    def makeFancyString(self, s: str) -> str:
        l = 0
        indices_to_delete = []

        for r in range(len(s)):
            while s[l] != s[r]:
                l += 1

            if r - l + 1 >= 3:
                indices_to_delete.append(r)

        list_s = list(s)

        for i, ch in enumerate(list_s):
            for j in indices_to_delete:
                if j == i:
                    list_s[j] = ""

        return "".join(list_s)


# O(n)
# Accepted
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        s_list = list(s)
        j = 2

        for i in range(2, len(s)):
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        return "".join(s_list[:j])
