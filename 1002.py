class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        tables = []
        res = []
        
        if len(A) == 1:
            return list(A[0])

        for idx, word in enumerate(A, start=1):
            table = dict()
            
            for char in word:
                if char in table.keys():
                    table[char] += 1
                else:
                    table[char] = 1
            
            tables.append(table)

        for letter in A[0]:
            if all(letter in table.keys() and table[letter] > 0 for table in tables):
                res.append(letter)
                
                for table in tables:
                    table[letter] -= 1

        return res                
