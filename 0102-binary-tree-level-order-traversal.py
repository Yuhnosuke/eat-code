# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(root):
            if not root:
                return

            q = deque()
            q.append(root)

            while q:
                nodes_in_current_level = len(q)
                tmp = []

                for _ in range(nodes_in_current_level):
                    node = q.popleft()
                    tmp.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                res.append(tmp)

        bfs(root)
        return res
