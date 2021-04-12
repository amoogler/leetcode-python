# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_org, queue_clo = collections.deque([original]), collections.deque([cloned])

        while queue_org:
            node_o = queue_org.pop()
            node_c = queue_clo.pop()

            if target is node_o:
                return node_c

            if node_o.left:
                queue_org.append(node_o.left)
                queue_clo.append(node_c.left)

            if node_o.right:
                queue_org.append(node_o.right)
                queue_clo.append(node_c.right)

        return None