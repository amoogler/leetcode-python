class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        res = 0

        for key, value in count1.items():
            if value == 1 and count2[key] == 1:
                res += 1

        return res
