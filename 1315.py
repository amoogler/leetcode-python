# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

                if node.val % 2 == 0:
                    if node.left.left:
                        res += node.left.left.val

                    if node.left.right:
                        res += node.left.right.val

            if node.right:
                queue.append(node.right)

                if node.val % 2 == 0:
                    if node.right.left:
                        res += node.right.left.val

                    if node.right.right:
                        res += node.right.right.val

        return res
