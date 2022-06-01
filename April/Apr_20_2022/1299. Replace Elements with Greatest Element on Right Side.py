class Solution:
    def replaceElements(self, arr):
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            prev = cur_max
            cur_max = max(arr[i], cur_max)
            arr[i] = prev

        return arr
