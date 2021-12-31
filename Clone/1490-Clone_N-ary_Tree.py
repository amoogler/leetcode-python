"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

# BFS Solution.
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root

        clone = {}
        queue = deque([root])
        clone[root] = Node(root.val, [])

        while queue:
            node = queue.popleft()

            for child in node.children:
                if child not in clone:
                    clone[child] = Node(child.val, [])
                    queue.append(child)

                clone[node].children.append(clone[child])

        return clone[root]

# DFS Recursive Solution.
class Solution:
    def __init__(self):
        self.clone = {}

    def cloneTree(self, root: 'None') -> 'None':
        # Base cases.
        if not root:
            return root

        if root in self.clone:
            return self.clone[root]

        clone_node = Node(root.val, [])
        self.clone[root] = clone_node

        if root.children:
            clone_node.children = [self.cloneTree(child) for child in root.children]

        return clone_node

