class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def findRow():
            left = 0
            right = len(matrix) - 1

            while left <= right:
                mid = (left + right) // 2
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid

                if matrix[mid][0] < target:
                    left = mid + 1

                else:
                    right = mid - 1

        def findCol(row):
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True

                if matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        row = findRow()
        if row == None:
            return False

        return findCol(row)
