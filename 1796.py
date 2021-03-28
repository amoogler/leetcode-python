import heapq as hq

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
        hq.heapify(digits)
        
        for i in range(len(digits) - 2):
            hq.heappop(digits)

        second = hq.heappop(digits)
        first = hq.heappop(digits)
        
        return second if second != first else -1
