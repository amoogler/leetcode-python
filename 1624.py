class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_length = -1

        if len(s) <= 1:
            return max_length

        mapping = dict()

        for idx, char in enumerate(s):
            if char in mapping:
                max_length = max(max_length, idx - mapping[char] - 1)
            else:
                mapping[char] = idx

        return max_length
