# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1, seq2 = [], []
        self.getLeafSequence(root1, seq1)
        self.getLeafSequence(root2, seq2)
        print(seq1, seq2)
        return ','.join(seq1) == ','.join(seq2)

    def getLeafSequence(self, node: TreeNode, sequence: List[int]):
        if not node:
            return

        if not node.left and not node.right:
            sequence.append(str(node.val))
            return

        self.getLeafSequence(node.left, sequence)
        self.getLeafSequence(node.right, sequence)
