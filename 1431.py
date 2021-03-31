from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        output = []
        
        for candy in candies:
            output.append((candy + extraCandies) >= max_candies)
        
        return output
