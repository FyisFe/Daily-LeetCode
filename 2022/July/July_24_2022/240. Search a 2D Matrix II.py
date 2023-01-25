class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            if matrix[r][0] > target:
                break
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[r][mid] == target:
                    return True
                if matrix[r][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
