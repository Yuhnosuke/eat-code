# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity: O(log^2 n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_height(node, child):
            h = 0
            while node:
                h += 1
                if child == "left":
                    node = node.left
                else:
                    node = node.right
            return h

        if not root:
            return 0

        left_height = get_height(root, "left")
        right_height = get_height(root, "right")

        if left_height == right_height:
            return 2**left_height - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Time Complexity; O(n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return

            ans += 1

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(root)
        return ans
