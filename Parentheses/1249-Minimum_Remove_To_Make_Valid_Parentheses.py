class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        right_remove = set()
        res = []

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    right_remove.add(idx)

        for idx, c in enumerate(s):
            if c == '(' and stack and stack[0] == idx:
                stack.pop(0)
                continue
            elif c == ')' and idx in right_remove:
                continue

            res.append(c)

        return ''.join(res)
