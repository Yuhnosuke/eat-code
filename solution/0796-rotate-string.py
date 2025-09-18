class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        q = deque([])

        for ch in s:
            q.append(ch)

        N = len(s)

        while N:
            q.append(q.popleft())

            if "".join(q) == goal:
                return True

            N -= 1

        return False
