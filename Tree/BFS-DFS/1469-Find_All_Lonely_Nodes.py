# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS solution.
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely = []

        if not root:
            return lonely

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if node.left and not node.right:
                lonely.append(node.left.val)
            elif node.right and not node.left:
                lonely.append(node.right.val)

        return lonely

# DFS solution.
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.lonely = []

        if not root:
            return lonely

        self.dfs(root)
        return self.lonely

    def dfs(self, node: TreeNode) -> None:
        # Base cases.
        if node.left and not node.right:
            self.lonely.append(node.left.val)
        elif node.right and not node.left:
            self.lonely.append(node.right.val)

        # Recusive steps.
        if node.left:
            self.dfs(node.left)

        if node.right:
            self.dfs(node.right)
