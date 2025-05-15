# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            if not root:
                return

            q = deque()
            q.append(root)

            while q:
                nodes_in_current_level = len(q)

                for i in range(nodes_in_current_level):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                    if i == nodes_in_current_level - 1:
                        res.append(node.val)

        bfs(root)
        return res
