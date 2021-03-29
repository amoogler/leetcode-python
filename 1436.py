from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapping = dict()
        destination = ''
        
        for path in paths:
            mapping[path[0]] = path[1]
            
        for path in paths:
            if path[1] not in mapping.keys():
                destination = path[1]
                break
        
        return destination
  