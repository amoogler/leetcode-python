# 1D presum cache solution with time complexity as O(m).
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row_presum = defaultdict(list)

        for i in range(len(matrix)):
            self.row_presum[i].append(0)
            run_sum = 0

            for j in range(len(matrix[0])):
                run_sum += matrix[i][j]
                self.row_presum[i].append(run_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for i in range(row1, row2 + 1):
            total += self.row_presum[i][col2 + 1] - self.row_presum[i][col1]

        return total

# Smarter cache to make time complexity as O(1).
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
