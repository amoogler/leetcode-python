class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [0] * len(words)

        for word in words:
            res[int(word[-1]) - 1] = word[:-1]

        return ' '.join(res)
