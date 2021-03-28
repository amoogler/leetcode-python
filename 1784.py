class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False

        for i in range(1, len(s)):
            if s[i] == '1':
                if seen_zero:
                    return False
            else:
                seen_zero = True

        return True
