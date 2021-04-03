class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        word = list(s)
        
        while start < end:
            if word[start] in vowels and word[end] in vowels:
                word[start], word[end] = word[end], word[start]
                start += 1
                end -= 1
            elif word[start] in vowels:
                end -= 1
            elif word[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        
        return ''.join(word)
