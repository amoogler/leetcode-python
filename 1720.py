class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]

        for num in encoded:
            res.append(num ^ res[-1])

        return res
