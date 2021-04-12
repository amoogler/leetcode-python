# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         postorder_nodes = []
#         self.postorder(root, postorder_nodes)
#         return postorder_nodes

#     def postorder(self, node: TreeNode, postorder_nodes: List[int]):
#         if node:
#             self.postorder(node.left, postorder_nodes)
#             self.postorder(node.right, postorder_nodes)
#             postorder_nodes.append(node.val)

# Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder_nodes, stack = [], []
        current, prev = root, None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack[-1]

                if current.right and current.right != prev:
                    current = current.right
                else:
                    postorder_nodes.append(current.val)
                    stack.pop()
                    prev = current
                    current = None

        return postorder_nodes
