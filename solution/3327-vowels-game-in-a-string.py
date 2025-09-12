class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for ch in s:
            if ch in "aiueo":
                return True

        return False
