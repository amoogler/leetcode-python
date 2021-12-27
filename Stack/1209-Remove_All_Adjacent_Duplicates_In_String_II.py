class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k - 1:
                stack.pop()
            else:
                if not stack or stack[-1][0] != c:
                    stack.append((c, 1))
                else:
                    value, frequency = stack.pop()
                    stack.append((value, frequency + 1))

        return ''.join([e[0] * e[1] for e in stack])
