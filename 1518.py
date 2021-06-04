class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        total, left_empty, to_drink = 0, 0, num_bottles

        while to_drink != 0:
            # Drink and count.
            drunk = to_drink
            total += drunk

            # Update number of drinks we can get for next round.
            to_drink = (drunk + left_empty) // num_exchange

            # Update number of empty bottles left after exchange.
            left_empty = (drunk + left_empty) % num_exchange

        return total
