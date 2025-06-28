# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursively
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            ans.append(root.val)

        dfs(root)
        return ans


# iteratively
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        node_stack = [root]
        visited_stack = [False]

        while node_stack:
            curr = node_stack.pop()
            is_visited = visited_stack.pop()

            if curr:
                if is_visited:
                    ans.append(curr.val)
                else:
                    node_stack.append(curr)
                    visited_stack.append(True)

                    node_stack.append(curr.right)
                    visited_stack.append(False)

                    node_stack.append(curr.left)
                    visited_stack.append(False)

        return ans
