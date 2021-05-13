class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        i = 0

        for num in encoded:
            res.append(num ^ res[i])
            i += 1

        return res
