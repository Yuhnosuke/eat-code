# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        return res[k - 1]


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res = -1
#         count = k

#         def inorder(root):
#             nonlocal res
#             nonlocal count

#             if not root:
#                 return

#             inorder(root.left)

#             count -= 1
#             if count == 0:
#                 res = root.val

#             inorder(root.right)

#         inorder(root)

#         return res
