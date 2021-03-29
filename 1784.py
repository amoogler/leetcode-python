class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False

        for i in range(1, len(s)):
            if s[i] == '1' and seen_zero:
                return False
            elif s[i] == '0':
                seen_zero = True

        return True
