class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter([s[i : i + minSize] for i in range(len(s) - minSize + 1)])
        occurrences = [count[sub_str] for sub_str in count if len(set(sub_str)) <= maxLetters]
        return max(occurrences) if occurrences else 0
