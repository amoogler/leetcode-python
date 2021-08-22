class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.mapping = defaultdict(list)

        for idx, word in enumerate(wordsDict):
            self.mapping[word].append(idx)


    def shortest(self, word1: str, word2: str) -> int:
        indexes1, indexes2 = self.mapping[word1], self.mapping[word2]
        min_distance = float('inf')
        i, j = 0, 0

        while i < len(indexes1) and j < len(indexes2):
            idx1, idx2 = indexes1[i], indexes2[j]

            if idx1 < idx2:
                min_distance = min(min_distance, idx2 - idx1)
                i += 1
            else:
                min_distance = min(min_distance, idx1 - idx2)
                j += 1

        return min_distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
