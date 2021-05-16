value_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = value_map[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if value_map[s[i]] < value_map[s[i + 1]]:
                total -= value_map[s[i]]
            else:
                total += value_map[s[i]]

        return total
