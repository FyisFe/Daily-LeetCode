class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(array, target):

            low = 0
            high = len(array)

            while low < high:
                mid = (low + high) // 2

                if array[mid] == target:
                    return mid

                elif array[mid] < target:
                    low = mid + 1

                elif array[mid] > target:
                    high = mid

            return -1

        for i in matrix:
            if i[0] <= target:
                if search(i, target) != -1:
                    return True

        return False
