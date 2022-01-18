# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This problem is to deserialize a tree from given string.
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack, num = [TreeNode(-1)], ''

        for i, c in enumerate(s):
            if c == ')': # tree is done
                stack.pop()
            elif c != '(': # digit or '-'
                num += c

                if i + 1 == len(s) or not s[i + 1].isdigit():
                    node = TreeNode(int(num))
                    parent = stack[-1]

                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node

                    stack.append(node)
                    num = ''

        return stack[0].left
