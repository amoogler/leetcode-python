class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, count = [], 0

        for c in S:
            if c == '(' and count > 0:
                res.append(c)
            elif c == ')' and count > 1:
                res.append(c)

            count += 1 if c == '(' else -1

        return ''.join(res)
