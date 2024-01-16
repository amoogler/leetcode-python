class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_1, index_2, min_distance = -1, -1, len(wordsDict)

        for idx, word in enumerate(wordsDict):
            if word == word1:
                index_1 = idx

            if word == word2:
                index_2 = idx

            if (word == word1 or word == word2) and (index_1 != -1 and index_2 != -1):
                min_distance = min(min_distance, abs(index_1 - index_2))

        return min_distance
