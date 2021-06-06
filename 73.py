class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for i in range(R):
            if matrix[i][0] == 0:
                row_zero = True

        for j in range(C):
            if matrix[0][j] == 0:
                col_zero = True

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for i in range(R):
                matrix[i][0] = 0

        if col_zero:
            for j in range(C):
                matrix[0][j] = 0
