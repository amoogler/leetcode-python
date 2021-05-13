class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev_idx = float('-inf')
        res = []

        for idx, char in enumerate(s):
            if char == c:
                prev_idx = idx

            res.append(idx - prev_idx)

        prev_idx = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev_idx = i

            res[i] = min(res[i], prev_idx - i)

        return res