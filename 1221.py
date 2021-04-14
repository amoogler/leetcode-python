class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, count = 0, 0

        for char in s:
            if char == 'L':
                count += 1
            elif char == 'R':
                count -= 1

            if count == 0:
                res += 1

        return res
