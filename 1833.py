class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        count = 0

        for i, coin in enumerate(sorted_costs):
            coins -= coin

            if coins >= 0:
                count += 1
            else:
                break

        return count