# Given the number of bags,
# Returns the minimum capacity of each bag,
# so that we can put items one by one into all bags.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            if self.doable(weights, mid, days):
                right = mid
            else:
                left = mid + 1

        return left

    def doable(self, weights: List[int], capacity: int, days: int) -> bool:
        need, curr = 1, 0

        for weight in weights:
            if curr + weight > capacity:
                need += 1
                curr = 0

            curr += weight

            if need > days:
                return False

        return True
