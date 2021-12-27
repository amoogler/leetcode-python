class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for sentence in sentences:
            res = max(res, len(sentence.split(' ')))

        return res
