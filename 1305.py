# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def pushleft(node: TreeNode, stack: List[TreeNode]):
            while node:
                stack.append(node)
                node = node.left

        def addToRes(stack: List[TreeNode], res: List[int]):
            node = stack.pop()
            res.append(node.val)
            pushleft(node.right, stack)

        res, stack1, stack2 = [], [], []
        pushleft(root1, stack1)
        pushleft(root2, stack2)

        while stack1 or stack2:
            if stack1 and stack2:
                if stack1[-1].val < stack2[-1].val:
                    addToRes(stack1, res)
                else:
                    addToRes(stack2, res)
            else:
                if stack1:
                    addToRes(stack1, res)
                else:
                    addToRes(stack2, res)

        return res