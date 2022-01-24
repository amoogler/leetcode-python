# Only 5 possible input we need to pay attention.
# 1. digit: it should be one digit from the current number
# 2. '+': number is over, we can add the previous number and start a new number
# 3. '-': same as above
# 4. '(': push the previous result and the sign into stack, set result to 0, just calculate the new result within parenthesis
# 5. ')': pop out the top two elements from stack, first one is the sign before this pair of parenthesis, second one is the
# temporary result before this pair of parenthesis. We add them together.

class Solution:
    def calculate(self, s: str) -> int:
        def getInteger(p, start_ch, s, N):
            num = int(start_ch)

            while p < N and s[p].isdigit():
                num = num * 10 + int(s[p])
                p += 1

            return num, p

        N, sign, res = len(s), 1, 0
        stack = []
        p = 0

        while p < N:
            ch = s[p]
            p += 1

            if ch.isdigit():
                num, p = getInteger(p, ch, s, N)
                res += (num * sign)
            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res = (res * stack.pop() + stack.pop())

        return res
