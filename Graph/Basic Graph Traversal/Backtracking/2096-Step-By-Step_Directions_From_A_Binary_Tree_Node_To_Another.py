# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Graph + Backtracking
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.graph = defaultdict(list)
        queue = deque([root])
        self.min_length = float('inf')
        self.paths = []

        while queue:
            node = queue.popleft()

            if node.left:
                self.graph[node.val].append((node.left.val, 'L'))
                self.graph[node.left.val].append((node.val, 'U'))
                queue.append(node.left)

            if node.right:
                self.graph[node.val].append((node.right.val, 'R'))
                self.graph[node.right.val].append((node.val, 'U'))
                queue.append(node.right)

        self.backtrack(startValue, destValue, [], set())

        for path in self.paths:
            if len(path) == self.min_length:
                return ''.join(path)

    def backtrack(self, start: int, end: int, path: list, visited: set) -> None:
        if start == end:
            res = path[:]
            self.min_length = min(self.min_length, len(res))
            self.paths.append(path[:])
            return

        if start in visited:
            return

        visited.add(start)

        for value, direction in self.graph[start]:
            path.append(direction)
            self.backtrack(value, end, path, visited)
            path.pop()
