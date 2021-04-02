from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])       
        merged = []
        current = sorted_intervals[0]
        
        for incoming_start, incoming_end in sorted_intervals[1:]:
            current_start = current[0]
            current_end = current[1]

            if incoming_start > current_end:
                merged.append(current)
                current = [incoming_start, incoming_end]
            else:
                current = [current_start, max(current_end, incoming_end)]
        
        merged.append(current)
        
        return merged
