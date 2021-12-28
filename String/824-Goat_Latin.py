class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = []
        words = sentence.split(' ')

        for idx, word in enumerate(words):
            if word[0] in vowels:
                res.append(word + 'ma' + 'a' * (idx + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (idx + 1))

        return ' '.join(res)
