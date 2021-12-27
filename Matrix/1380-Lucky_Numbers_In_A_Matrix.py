class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minimum_row, maximum_col = [], []
        res = []

        for i in range(len(matrix)):
            minimum_row.append(min(matrix[i]))

        for i in range(len(matrix[0])):
            col_max = float('-inf')

            for j in range(len(matrix)):
                col_max = max(col_max, matrix[j][i])

            maximum_col.append(col_max)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == minimum_row[i] and matrix[i][j] == maximum_col[j]:
                    res.append(matrix[i][j])

        return res
