class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []

        def remove(s: str, i_start: int, j_start: int, op: str, cp: str) -> None:
            op_count, cp_count = 0, 0

            for i in range(i_start, len(s)):
                if s[i] == op:
                    op_count += 1
                elif s[i] == cp:
                    cp_count += 1

                # We have extra closed parentheses to remove.
                if cp_count > op_count:
                    for j in range(j_start, i + 1):

                        # We have valid number of closed parentheses through i.
                        # Only remove the first cp at j == j_start to prevent duplicates.
                        if j > j_start and s[j] == s[j - 1]:
                            continue

                        if s[j] == cp:
                            remove(s[0:j] + s[j + 1:len(s)], i, j, op, cp)
                    return

            # No invalid closed parentheses detected. Now check the opposite direction
            # to remove additional op.
            reversed_s = s[::-1]

            if op == '(':
                remove(reversed_s, 0, 0, ')', '(')
            else:
                # Reverse back again.
                res.append(reversed_s)

        remove(s, 0, 0, '(', ')')
        return res
