class Node:

    def __init__(self, total, l, r):
        self.sum = total
        # index
        self.l = l
        self.r = r
        # pointer
        self.left = None
        self.right = None


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)

        root = Node(0, l, r)
        m = (l + r) // 2

        root.left = self.build(nums, l, m)
        root.right = self.build(nums, m + 1, r)

        root.sum = root.left.sum + root.right.sum

        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.l == root.r:
            root.sum = val
            return

        m = (root.l + root.r) // 2

        if index > m:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)

        root.sum = root.left.sum + root.right.sum

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        if L == root.l and R == root.r:
            return root.sum

        m = (root.l + root.r) // 2

        if L > m:
            return self.query_helper(root.right, L, R)
        elif R <= m:
            return self.query_helper(root.left, L, R)
        else:
            return self.query_helper(root.left, L, m) + self.query_helper(
                root.right, m + 1, R
            )
