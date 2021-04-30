class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return ''.join([c for c in s if c not in vowels])
