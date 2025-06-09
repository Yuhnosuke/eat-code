# brute force 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(i: int, curr: str) -> None:
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            s, e = 0, 0
            for ch in curr:
                if ch == "(":
                    s += 1
                else:
                    e += 1

            if s < n:
                dfs(i + 1, curr + "(")

            if s > e:
                dfs(i + 1, curr + ")")

        dfs(0, "")
        return ans


# brute force 2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(opens: int, closes: int, curr: str) -> None:
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if opens < n:
                dfs(opens + 1, closes, curr + "(")

            if opens > closes:
                dfs(opens, closes + 1, curr + ")")

        dfs(0, 0, "")
        return ans


# backtrack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(opens: int, closes: int, curr: List[str]) -> None:
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return

            if opens < n:
                curr.append("(")
                dfs(opens + 1, closes, curr)
                curr.pop()

            if opens > closes:
                curr.append(")")
                dfs(opens, closes + 1, curr)
                curr.pop()

        ans = []
        dfs(0, 0, [])
        return ans
