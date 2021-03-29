class Solution:
    def toLowerCase(self, str: str) -> str:
        lower_letters = []
        
        for char in str:
            if ord(char) <= ord('Z') and ord(char) >= ord('A'):
                lower_letters.append(chr(ord(char) - ord('A') + ord('a')))
            else:
                lower_letters.append(char)
        
        return ''.join(lower_letters)
 