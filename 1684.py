from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0      
        allowed = set(allowed)
        
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break
                    
            if consistent:
                count += 1
                
        return count
 