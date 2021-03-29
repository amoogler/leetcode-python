class Solution:
    def toLowerCase(self, str: str) -> str:
        lower_letters = []
        
        for char in str:
            if ord('A') <= ord(char) <= ord('Z'):
                lower_letters.append(chr(ord(char) - ord('A') + ord('a')))
            else:
                lower_letters.append(char)
        
        return ''.join(lower_letters)
