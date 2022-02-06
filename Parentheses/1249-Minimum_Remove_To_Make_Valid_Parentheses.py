class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        # Remove unmatched ')'s.
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        # Remove left over '('s.
        while stack:
            s[stack.pop()] = ''

        return ''.join(s)
