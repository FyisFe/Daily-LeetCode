class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        n = len(arr)
        while idx < len(arr):
            if arr[idx] == 0:
                for i in range(n - 1, idx, -1):
                    arr[i] = arr[i - 1]
                idx += 1
            idx += 1
