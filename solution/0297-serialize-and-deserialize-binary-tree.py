# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"

        serialized = []
        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                serialized.append("N")
            else:
                serialized.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
