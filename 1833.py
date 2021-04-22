class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0

        for cost in sorted(costs):
            coins -= cost

            if coins >= 0:
                count += 1
            else:
                break

        return count