# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case 1
        if not root:
            return False

        # base case 2
        delta = targetSum - root.val
        if not root.left and not root.right and delta == 0:
            return True

        return self.hasPathSum(root.left, delta) or self.hasPathSum(root.right, delta)
