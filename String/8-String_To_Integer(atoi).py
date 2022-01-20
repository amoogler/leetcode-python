# Discards all leading whitespaces.
# Determine the sign of the ingeter.
# Overflow
# Invalid input

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        num = 0

        if not s:
            return num

        # Discards all leading whitespaces.
        while i < len(s) and s[i] == ' ':
            i += 1

        # Determine the sign of the integer
        if i < len(s):
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                sign = 1
                i += 1

        while i < len(s) and s[i].isdigit():
            # Handle overflow.
            max_value = pow(2, 31)

            if num > max_value // 10 or (num == max_value // 10 and int(s[i]) > 7):
                return (max_value - 1) if sign == 1 else -max_value

            num  = 10 * num + int(s[i])
            i += 1

        return num * sign
