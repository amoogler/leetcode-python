from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.compare)        
        merged = []
        current = intervals[0]
        
        for incoming in intervals[1:]:
            if incoming[0] > current[1]:
                merged.append(current)
                current = incoming
            else:
                current = [current[0], max(current[1], incoming[1])]
        
        merged.append(current)
        
        return merged               
    
    def compare(self, interval: List[int]) -> int:
        return interval[0]
 