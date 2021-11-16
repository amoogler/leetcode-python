class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if not s:
            return True

        count = Counter(s)
        return len(set(count.values())) == 1
