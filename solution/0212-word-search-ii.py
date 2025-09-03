class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add_word(word)

        rows = len(board)
        columns = len(board[0])

        ans = set()
        visited = set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == columns
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                ans.add(word)

            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = dy + r, dx + c
                dfs(nr, nc, node, word)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(columns):
                dfs(r, c, root, "")
        return list(ans)
