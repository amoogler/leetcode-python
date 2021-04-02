from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = set()   
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            trans.add(''.join([MORSE[ord(char) - ord('a')] for char in word]))
            
        return len(trans)
