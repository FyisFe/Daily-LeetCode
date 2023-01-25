class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        ans = [[None] * row for _ in range(col)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
