"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Time complexity: O(n), Space complexity: O(n) solution.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        clone = {}
        node = head

        while node:
            if node not in clone:
                clone[node] = Node(node.val, None, None)

            if node.next:
                if node.next not in clone:
                    clone[node.next] = Node(node.next.val, None, None)

                clone[node].next = clone[node.next]

            if node.random:
                if node.random not in clone:
                    clone[node.random] = Node(node.random.val, None, None)

                clone[node].random = clone[node.random]

            node = node.next

        return clone[head]
