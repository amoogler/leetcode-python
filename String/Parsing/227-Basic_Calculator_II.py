# For '+' and '-', the expression is evaluated based on the precedence of
# the next operation.
# For '*' and '/', the expression is evaluated irrespective of next operation.

class Solution:
    def calculate(self, s: str) -> int:
        def getInteger(p, start_ch, s, N):
            num = int(start_ch)

            while p < N and s[p].isdigit():
                num = num * 10 + int(s[p])
                p += 1

            return num, p

        p = 0
        operator = '+'
        N = len(s)
        operators = {'+', '-', '*', '/'}
        stack = []
        curr_num = 0
        res = 0

        while p < N:
            ch = s[p]
            p += 1

            if ch.isdigit():
                curr_num, p = getInteger(p, ch, s, N)

            if ch in operators or p == N:
                if operator == '+':
                    stack.append(curr_num)
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '*':
                    stack.append(stack.pop() * curr_num)
                elif operator == '/':
                    stack.append(int(stack.pop() / curr_num))

                operator = ch
                curr_num = 0

        return sum(stack)
