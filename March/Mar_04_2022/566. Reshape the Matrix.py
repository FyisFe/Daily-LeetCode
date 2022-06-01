class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m = len(mat)
        n = len(mat[0])

        if r * c != m * n:
            return mat

        return [
            [
                mat[(row * c + col) // n][(row * c + col) - ((row * c + col) // n) * n]
                for col in range(c)
            ]
            for row in range(r)
        ]
