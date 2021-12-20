# Sweep-line technique.
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        d = [0] * 52
        total = 0

        for start, end in ranges:
            d[start] += 1
            d[end + 1] -= 1

        for i in range(1, right + 1):
            total += d[i]

            if i >= left and total < 1:
                return False

        return True
