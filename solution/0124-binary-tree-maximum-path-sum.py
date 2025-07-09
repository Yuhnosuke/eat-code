# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curr = root.val

        def dfs(root):
            nonlocal curr

            if not root:
                return 0

            left_sum = dfs(root.left)
            if left_sum < 0:
                left_sum = 0

            right_sum = dfs(root.right)
            if right_sum < 0:
                right_sum = 0

            curr = max(curr, left_sum + right_sum + root.val)

            # pass bigger sum of one of subtree to parent node
            # because  of the `path`
            return max(left_sum, right_sum) + root.val

        dfs(root)
        return curr
