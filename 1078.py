class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        N = len(words)
        res = []

        if N <= 2:
            return res

        for i in range(2, N):
            if words[i - 1] == second and words[i - 2] == first:
                res.append(words[i])

        return res
