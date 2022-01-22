# It essentially the same as finding the first bad version.
# e.g. look for the position of last 1 in 1, 1, 1, 1, 0, 0, 0, 0.
# We'll use binary search to find the index of first 0, then minus 1.
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, 10 ** 5 + 1

        while left < right:
            mid = (left + right) // 2

            if not self.isCutPossible(ribbons, mid, k):
                right = mid
            else:
                left = mid + 1

        return left - 1

    def isCutPossible(self, ribbons: List[int], length: int, k: int) -> bool:
        count = 0

        for ribbon in ribbons:
            count += (ribbon // length)

            if count >= k:
                return True

        return False
