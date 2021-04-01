class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        power = 1
        current = s[0]
        
        for char in s[1:]:
            if current == char:
                power += 1
            else:
                max_power = max(power, max_power)
                current = char
                power = 1
        
        return max(power, max_power)
