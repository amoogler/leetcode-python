# Simulate rules.
# The approach to to enumerate all possible types of characters and
# layout the rules upon seeing them.
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit, seen_exponent, seen_dot = False, False, False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c == '+' or c == '-':
                # For a sign, it has to be either the first char or right after an exponent.
                # Otherwise, invalid.
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif c == 'e' or c == 'E':
                # For exponent, it has to be appeared once and after a digit is seen.
                # Otherwise, invalid.
                if seen_exponent or not seen_digit:
                    return False

                seen_exponent = True
                seen_digit = False
            elif c == '.':
                # For a dot, it has to be appeared once and it cannot be seen after an exponent.
                # Otherwise, invalid.
                if seen_dot or seen_exponent:
                    return False

                seen_dot = True
            else:
                # For all other cases, invalid.
                return False

        # A valid number has to have at least one digit.
        return seen_digit
