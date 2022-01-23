class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        left, right = 1, total

        while left < right:
            mid = (left + right) // 2

            if not self.doable(piles, mid, h):
                left = mid + 1
            else:
                right = mid

        return left

    def doable(self, piles: List[int], k: int, h: int) -> bool:
        hours = 0

        for pile in piles:
            hours_taken, leftover = divmod(pile, k)
            hours += hours_taken

            if leftover > 0:
                hours += 1

            if hours > h:
                return False

        return True
