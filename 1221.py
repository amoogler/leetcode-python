class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, stack = 0, []

        for char in s:
            if stack and char != stack[-1]:
                stack.pop()
            else:
                stack.append(char)

            if not stack:
                count += 1

        return count
