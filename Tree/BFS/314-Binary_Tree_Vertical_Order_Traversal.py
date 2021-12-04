# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        columnTable = defaultdict(list)
        min_column, max_column = 0, 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left:
                queue.append((node.left, column - 1))

            if node.right:
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]
