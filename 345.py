class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = set("aeiouAEIOU")
        word = list(s)
        
        while start < end:
            while start < end and word[start] not in vowels:
                start += 1

            while start < end and word[end] not in vowels:
                end -= 1

            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
        return ''.join(word)
