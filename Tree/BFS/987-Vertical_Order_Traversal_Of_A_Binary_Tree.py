# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columnTable = defaultdict(list)
        queue = deque([(root, 0, 0)])
        res = []

        while queue:
            node, row, column = queue.popleft()
            columnTable[column].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, column - 1))

            if node.right:
                queue.append((node.right, row + 1, column + 1))

        for c in sorted(columnTable.keys()):
            sorted_list = sorted(columnTable[c])
            res.append([item[1] for item in sorted_list])

        return res
