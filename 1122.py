from collections import defaultdict
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_set = set(arr1)
        arr2_set = set(arr2)
        only_arr1 = sorted([e for e in arr1_set if e not in arr2_set])
        num_pos = defaultdict(int)
        
        for idx, element in enumerate(arr2):
            num_pos[element] = idx
        
        num_pos_length = len(num_pos)

        for idx, element in enumerate(only_arr1):
            num_pos[element] = num_pos_length + idx
        
        return sorted(arr1, key=lambda x : num_pos[x])
