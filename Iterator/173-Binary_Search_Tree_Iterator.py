# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushleft(root, self.stack)

    def pushleft(self, node: TreeNode, stack: List[int]):
        while node:
            stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.pushleft(node.right, self.stack)
        return node.val

    def hasNext(self) -> bool:
        return self.stack
