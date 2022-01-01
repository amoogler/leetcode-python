# Stack based solution, time in O(m + n), space in O(m + n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        self.simplify(stack1, s)
        self.simplify(stack2, t)

        if len(stack1) != len(stack2):
            return False

        for chr1, chr2 in zip(stack1, stack2):
            if chr1 != chr2:
                return False

        return True

    def simplify(self, stack: List[str], string: str) -> None:
        for c in string:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

# Two pointers based solution, time in O(n), space in O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            # If expecting to compare char vs None, return False.
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True
