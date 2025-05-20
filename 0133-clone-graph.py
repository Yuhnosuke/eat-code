"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        original_cloned_map = {}

        def dfs(node):
            if node in original_cloned_map:
                return original_cloned_map[node]

            cloned = Node(node.val)
            original_cloned_map[node] = cloned

            for neighbor in node.neighbors:
                cloned.neighbors.append(dfs(neighbor))

            return cloned

        return dfs(node)
