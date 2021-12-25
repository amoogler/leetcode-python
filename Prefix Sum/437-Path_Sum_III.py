# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count

            if not node:
                return

            curr_sum += node.val

            if curr_sum == targetSum:
                count += 1

            count += d[curr_sum - targetSum]

            d[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            d[curr_sum] -= 1

        count = 0
        d = defaultdict(int)
        preorder(root, 0)
        return count
