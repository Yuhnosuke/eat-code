class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i: int, opens: int, memo: dict) -> bool:
            if opens < 0:
                return False

            if i == len(s):
                return opens == 0

            if (i, opens) in memo:
                return memo[(i, opens)]

            if s[i] == "(":
                result = dfs(i + 1, opens + 1, memo)
            elif s[i] == ")":
                result = dfs(i + 1, opens - 1, memo)
            else:
                result = (
                    dfs(i + 1, opens, memo)
                    or dfs(i + 1, opens + 1, memo)
                    or dfs(i + 1, opens - 1, memo)
                )

            memo[(i, opens)] = result
            return result

        memo = {}
        return dfs(0, 0, memo)
