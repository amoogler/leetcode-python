class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = []
        
        for char in address:
            if char == '.':
                defang.append('[.]')
            else:
                defang.append(char)
        
        return ''.join(defang)
