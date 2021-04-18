class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_idx = collections.defaultdict(list)
        first_idx = len(s)

        for i, letter in enumerate(s):
            letter_idx[letter].append(i)

        for value in letter_idx.values():
            if len(value) == 1:
                first_idx = min(value[0], first_idx)

        return first_idx if first_idx != len(s) else -1
