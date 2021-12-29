# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder_nodes = []
        self.postorder(root, postorder_nodes)
        return postorder_nodes

    def postorder(self, node: TreeNode, postorder_nodes: List[int]):
        if node:
            self.postorder(node.left, postorder_nodes)
            self.postorder(node.right, postorder_nodes)
            postorder_nodes.append(node.val)

# Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # First apprearance is for adding node.
        # Second apprearance is for traversal.
        postorder_nodes, stack = [], [root, root]

        while stack:
            node = stack.pop()

            if stack and stack[-1] == node:
                if node.right:
                    stack.extend([node.right, node.right])

                if node.left:
                    stack.extend([node.left, node.left])
            else:
                postorder_nodes.append(node.val)

        return postorder_nodes
