class Solution:
    def diagonalSum(self, mat) -> int:
        m = len(mat)
        res = 0
        for i in range(m):
            res += mat[i][i]
            mat[i][i] = 0

        for i in range(m - 1, -1, -1):
            res += mat[i][m - i - 1]

        return res
