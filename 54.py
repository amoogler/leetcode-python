class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if not matrix:
            return res

        R_BEG, R_END, C_BEG, C_END = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while R_BEG <= R_END and C_BEG <= C_END:
            for i in range(C_BEG, C_END + 1):
                res.append(matrix[R_BEG][i])

            R_BEG += 1

            for i in range(R_BEG, R_END + 1):
                res.append(matrix[i][C_END])

            C_END -= 1

            if R_BEG <= R_END:
                for i in range(C_END, C_BEG - 1, -1):
                    res.append(matrix[R_END][i])

                R_END -= 1

            if C_BEG <= C_END:
                for i in range(R_END, R_BEG - 1, -1):
                    res.append(matrix[i][C_BEG])

                C_BEG += 1

        return res
