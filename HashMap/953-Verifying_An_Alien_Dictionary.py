class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def isSorted(word1: str, word2: str) -> bool:
            for c1, c2 in zip(word1, word2):
                if order_map[c1] != order_map[c2]:
                    return order_map[c1] < order_map[c2]

            return len(word1) <= len(word2)

        order_map = {alphabet: idx for idx, alphabet in enumerate(order)}

        return all(isSorted(word1, word2) for word1, word2 in zip(words, words[1:]))
