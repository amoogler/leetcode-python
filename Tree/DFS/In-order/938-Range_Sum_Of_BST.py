# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def pushleft(stack: List[TreeNode], node: TreeNode):
            while node:
                stack.append(node)
                node = node.left
            
        stack, range_sum = [], 0
        pushleft(stack, root)

        while stack:
            node = stack.pop()
            pushleft(stack, node.right)
            
            if low <= node.val <= high:
                range_sum += node.val
            elif node.val > high:
                break
        
        return range_sum

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order(node):
            nonlocal range_sum

            if node:
                in_order(node.left)

                if low <= node.val <= high:
                    range_sum += node.val

                in_order(node.right)

        range_sum = 0
        in_order(root)
        return range_sum
