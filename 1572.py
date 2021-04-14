class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum, square_side = 0, len(mat)

        # upper left to lower right
        for i in range(square_side):
            total_sum += mat[i][i]

        # upper right to lower left
        for i, j in zip(range(square_side), range(square_side - 1, -1, -1)):
            if i != j:
                total_sum += mat[i][j]

        return total_sum
