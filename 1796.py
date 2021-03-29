class Solution:
    def secondHighest(self, s: str) -> int:
        digits_set = set()
        for char in s:
            if char.isnumeric():
                digit = int(char)
                digits_set.add(digit)

        if len(digits_set) < 2:
            return -1
                
        digits = list(digits_set)
        digits.sort()
        
        return digits[len(digits) - 2]
