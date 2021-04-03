from collections import defaultdict
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        only_arr1 = sorted([e for e in arr1 if e not in arr2])
        num_pos = defaultdict(lambda: 0)
        
        for idx, element in enumerate(arr2):
            num_pos[element] = idx
        
        num_pos_length = len(num_pos)

        for idx, element in enumerate(only_arr1):
            num_pos[element] = num_pos_length + idx
        
        return sorted(arr1, key=lambda x : num_pos[x])
