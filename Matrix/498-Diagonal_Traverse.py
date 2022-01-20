class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])
        res = []

        if M == 0 or N == 0:
            return res

        r, c = 0, 0

        for i in range(M * N):
            res.append(mat[r][c])

            # Moving up for even numberred level, moving down for odd numberred level.
            if (r + c) % 2 == 0:
                if c == N - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == M - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1

        return res
