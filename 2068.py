class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)
        max_diff = 0

        for k1, v1 in count1.items():
            diff = v1 if k1 not in count2 else abs(count2[k1] - v1)
            max_diff = max(max_diff, diff)

        for k2, v2 in count2.items():
            if k2 not in count1:
                max_diff = max(max_diff, v2)

        return max_diff <= 3
