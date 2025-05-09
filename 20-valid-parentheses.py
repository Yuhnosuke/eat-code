class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for ch in s:
            if ch in open_close_map.keys():
                stack.append(ch)
            else:
                if not stack:
                    return False

                popped = stack.pop()
                if open_close_map[popped] != ch:
                    return False

        return len(stack) == 0
