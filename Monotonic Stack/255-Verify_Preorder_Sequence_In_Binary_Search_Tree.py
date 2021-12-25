class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low_bound = float('-inf')

        for value in preorder:
            if value < low_bound:
                return False

            while stack and value > stack[-1]:
                low_bound = stack.pop()

            stack.append(value)

        return True
