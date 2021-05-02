class Solution:
    def checkValidString(self, s: str) -> bool:
        # possible number of open left brackets in [lo, hi].
        lo, hi = 0, 0

        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1

            if hi < 0:
                return False

            # Cannot continue making assumption based on lo < 0.
            # at position 2, e.g. '(**(' -> '())('.
            lo = max(0, lo)

        return lo == 0
