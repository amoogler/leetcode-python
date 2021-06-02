class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total, left_empty, to_drink = 0, 0, numBottles

        while to_drink != 0:
            # Drink and count.
            drunk = to_drink
            total += drunk

            # Compute how many new drinks we can get.
            to_drink = (drunk + left_empty) // numExchange

            # Compute how many empty bottles after exchange.
            left_empty = (drunk + left_empty) % numExchange

        return total
