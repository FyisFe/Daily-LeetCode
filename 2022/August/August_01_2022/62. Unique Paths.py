class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mat = [[0] * n for _ in range(m)]

        for i in range(m):
            mat[i][0] = 1

        for i in range(n):
            mat[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[m - 1][n - 1]
