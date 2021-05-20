class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows, res = [], []

        for i in range(len(mat)):
            rows.append((Counter(mat[i])[1], i))

        rows = sorted(rows, key=lambda x : x[0])

        for row in rows:
            res.append(row[1])

        return res[:k]
