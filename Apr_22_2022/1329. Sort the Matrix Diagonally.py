class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def matrix_sort(x, y):
            tmp = []
            i = 0
            while x + i < m and y + i < n:
                tmp.append(mat[x + i][y + i])
                i += 1

            tmp.sort()
            i = 0

            while x + i < m and y + i < n:
                mat[x + i][y + i] = tmp.pop(0)
                i += 1

        for x in range(m):
            matrix_sort(x, 0)

        for y in range(1, n):
            matrix_sort(0, y)

        return mat
