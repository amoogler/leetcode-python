class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if not matrix:
            return res

        r_beg, r_end, c_beg, c_end = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while r_beg <= r_end and c_beg <= c_end:
            for i in range(c_beg, c_end + 1):
                res.append(matrix[r_beg][i])

            r_beg += 1

            for i in range(r_beg, r_end + 1):
                res.append(matrix[i][c_end])

            c_end -= 1

            if r_beg <= r_end:
                for i in range(c_end, c_beg - 1, -1):
                    res.append(matrix[r_end][i])

                r_end -= 1

            if c_beg <= c_end:
                for i in range(r_end, r_beg - 1, -1):
                    res.append(matrix[i][c_beg])

                c_beg += 1

        return res
