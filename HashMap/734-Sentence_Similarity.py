class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarTable = set()

        for x1, y1 in similarPairs:
            similarTable.add((x1, y1))
            similarTable.add((y1, x1))

        return all(w1 == w2 or (w1, w2) in similarTable for w1, w2 in zip(sentence1, sentence2))
