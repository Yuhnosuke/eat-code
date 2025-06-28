class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build adjacency list
        adj = {}
        for word in words:
            for ch in word:
                adj[ch] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))

            # invalid case like "abc" comes after "ab"
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # define dfs
        visited = {}
        res = []

        # return True if visited in current path
        # return False if have not visited the node in current path
        def dfs(ch: str) -> bool:
            if ch in visited:
                return visited[ch]

            visited[ch] = True

            for nei in adj[ch]:
                if dfs(nei):
                    return True

            visited[ch] = False
            res.append(ch)

        # apply dfs
        for ch in adj:
            if dfs(ch):
                return ""

        # make order topological
        res.reverse()
        return "".join(res)
