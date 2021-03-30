from typing import List
from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = set([departure for departure, arrival in paths])
        res = ''
        
        for departure, arrival in paths:
            if arrival not in departures:
                res = arrival
                break
        
        return res
