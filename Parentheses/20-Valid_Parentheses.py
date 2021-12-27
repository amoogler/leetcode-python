class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif stack and stack[-1] == parentheses[char]:
                stack.pop()
            else:
                return False

        return not stack
