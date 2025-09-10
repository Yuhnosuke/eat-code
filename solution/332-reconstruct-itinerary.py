# Time Limit Exceeded
# O(E ** 2) where E is the number of edges
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        def dfs(src: str) -> bool:
            if len(ans) == len(tickets) + 1:
                return True

            if src not in graph:
                return False

            # not to update for iteration
            tmp = list(graph[src])

            for i, neighbor in enumerate(tmp):
                graph[src].pop(i)
                ans.append(neighbor)

                if dfs(neighbor):
                    return True

                # if not valid path, then backtrack
                graph[src].insert(i, neighbor)
                ans.pop()

            return False

        ans = ["JFK"]
        dfs("JFK")

        return ans
