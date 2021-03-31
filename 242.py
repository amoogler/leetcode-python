from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(lambda: 0)
        
        if len(s) != len(t):
            return False
        
        for char in s:
            table[char] += 1
        
        for char in t:
            if char not in table:
                return False

            table[char] -= 1
            
        return all(value == 0 for value in table.values())
