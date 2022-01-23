# DFS - Backtracking based solution.
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

# BFS based solution.
# Framing problem to a tree alike structure, e.g. ()) -> )), (), ()
# We can use a set to dedup.
# BFS guarantees to find the shortest path.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            count = 0

            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        queue = deque([s])
        seen = {s}

        while queue:
            queue_length = len(queue)
            valid_s = []

            for _ in range(queue_length):
                curr_s = queue.popleft()

                if isValid(curr_s):
                    valid_s.append(curr_s)
                    continue

                for i in range(len(curr_s)):
                    next_s = curr_s[:i] + curr_s[i + 1:]

                    if next_s not in seen:
                        queue.append(next_s)
                        seen.add(next_s)

            if valid_s:
                return valid_s

        return []
