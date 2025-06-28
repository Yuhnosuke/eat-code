# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        next = self.stack.pop()
        curr = next.right

        # if right exists, append to stack as long as left subtree exists
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return next.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
