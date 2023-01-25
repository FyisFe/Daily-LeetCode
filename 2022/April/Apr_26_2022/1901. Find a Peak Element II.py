class Solution:
    def findPeakGrid(self, mat):
        def isPeak(x, y):
            dirc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in dirc:
                nx = x + dx
                ny = y + dy

                if (
                    nx >= len(mat)
                    or nx < 0
                    or ny >= len(mat[0])
                    or ny < 0
                    or mat[nx][ny] < mat[x][y]
                ):
                    continue
                return False
            return True

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if isPeak(r, c):
                    return [r, c]
