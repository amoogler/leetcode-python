from collections import defaultdict
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        tables = []
        res = []
        
        if len(A) == 1:
            return list(A[0])

        for word in A[1:]:
            table = defaultdict(lambda: 0)
            
            for char in word:
                table[char] += 1
            
            tables.append(table)

        for letter in A[0]:
            if all(letter in table and table[letter] > 0 for table in tables):
                res.append(letter)
                
                for table in tables:
                    table[letter] -= 1

        return res                
