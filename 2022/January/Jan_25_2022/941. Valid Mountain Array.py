class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        peak = 0
        for i in range(1, len(arr)):
            # get the first strictly increasing peak
            if arr[i] < arr[i - 1]:
                peak = i - 1
                break
            # the list must be strictly increasing
            elif arr[i] == arr[i - 1]:
                return False

        # if peak = -1, there is no decreasing
        # if peak = 0, there is no increasing
        if peak == 0:
            return False

        # check if the rest of the array is strictly decreasing
        for i in range(peak, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True
