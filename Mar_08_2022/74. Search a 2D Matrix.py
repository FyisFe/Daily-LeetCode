class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1
        row = 0
        while row_left <= row_right:
            mid = (row_left + row_right) // 2
            if matrix[mid][0] > target:
                row_right = mid - 1

            elif matrix[mid][-1] < target:
                row_left = mid + 1

            else:
                row = mid
                break

        col_left = 0
        col_right = len(matrix[row]) - 1

        while col_left <= col_right:
            col_mid = (col_left + col_right) // 2
            if matrix[row][col_mid] < target:
                col_left = col_mid + 1
            elif matrix[row][col_mid] > target:
                col_right = col_mid - 1
            else:
                return True

        return False
