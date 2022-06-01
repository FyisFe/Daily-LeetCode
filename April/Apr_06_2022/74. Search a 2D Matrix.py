class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """
        consider the matrix as a 1d array, then binary search
        """
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
