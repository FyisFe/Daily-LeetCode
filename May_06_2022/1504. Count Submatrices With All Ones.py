class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        for r in range(1, rows):
            for c, (a, b) in enumerate(zip(mat[r], mat[r - 1])):
                if a and b:
                    mat[r][c] += b
        ans = 0
        for row in mat:
            for c in range(cols):
                min_val = row[c]
                for val in row[c:]:
                    if val == 0:
                        break
                    elif val < min_val:
                        min_val = val
                    ans += min_val
        return ans
