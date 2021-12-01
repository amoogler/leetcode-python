class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        N, M = len(matrix), len(matrix[0])

        for i in range(N - 1):
            for j in range(M - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        return True
