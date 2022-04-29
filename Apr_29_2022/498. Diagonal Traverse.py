class Solution:
    def findDiagonalOrder(self, mat):
        ans = []
        m = len(mat)
        n = len(mat[0])
        isReverse = False

        for row in range(m):
            tmp = []
            for j in range(row + 1):
                if j >= n:
                    break
                tmp.append(mat[row - j][j])
            if isReverse:
                ans += reversed(tmp)
            else:
                ans += tmp
            isReverse = not isReverse

        for col in range(1, n):
            tmp = []
            for j in range(n - col):
                if m - j - 1 < 0:
                    break
                tmp.append(mat[m - j - 1][col + j])

            if isReverse:
                ans += reversed(tmp)
            else:
                ans += tmp
            isReverse = not isReverse

        return ans
