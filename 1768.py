class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged, idx1, idx2 = [], 0, 0

        while idx1 < len(word1) or idx2 < len(word2):
            if idx1 < len(word1):
                merged.append(word1[idx1])

            if idx2 < len(word2):
                merged.append(word2[idx2])

            idx1 += 1
            idx2 += 1

        return ''.join(merged)
