# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return root

        clone = {}
        clone[root] = NodeCopy(root.val, None, None, None)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                if node.left not in clone:
                    clone[node.left] = NodeCopy(node.left.val, None, None, None)

                clone[node].left = clone[node.left]
                queue.append(node.left)

            if node.right:
                if node.right not in clone:
                    clone[node.right] = NodeCopy(node.right.val, None, None, None)

                clone[node].right = clone[node.right]
                queue.append(node.right)

            if node.random:
                if node.random not in clone:
                    clone[node.random] = NodeCopy(node.random.val, None, None, None)

                clone[node].random = clone[node.random]

        return clone[root]
