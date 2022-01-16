# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS (pre-order) based solution.
# DFS is preferred over BFS in this task, because the linkage of adjacent
# nodes will be retained in the serialized string, which makes deserialization
# easier.
class Codec:
    SPLITER = ","
    NULL = "n"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def pre_order(node, buffer):
            if not node:
                buffer.append(self.NULL)
                buffer.append(self.SPLITER)
            else:
                buffer.append(str(node.val))
                buffer.append(self.SPLITER)
                pre_order(node.left, buffer)
                pre_order(node.right, buffer)

        buffer = []
        pre_order(root, buffer)
        return ''.join(buffer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def buildTree(nodes):
            value = nodes.popleft()

            if value == self.NULL:
                return None
            else:
                node = TreeNode(int(value))
                node.left = buildTree(nodes)
                node.right = buildTree(nodes)
                return node

        nodes = deque(data.split(','))
        return buildTree(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
