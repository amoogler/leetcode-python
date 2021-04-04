class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coordinates_sum = ord(coordinates[0]) - ord('a') + 1 + int(coordinates[1])
        return coordinates_sum % 2 == 1