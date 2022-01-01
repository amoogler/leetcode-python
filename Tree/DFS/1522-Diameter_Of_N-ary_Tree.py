"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def getLongestPath(node: 'None') -> int:
            if not node:
                return 0

            nonlocal diameter
            highest, second_highest = 0, 0

            for child in node.children:
                path = getLongestPath(child)

                if path > second_highest and path > highest:
                    second_highest, highest = highest, path
                elif second_highest <= path <= highest:
                    second_highest = path

                diameter = max(diameter, highest + second_highest)

            return highest + 1

        getLongestPath(root)
        return diameter
