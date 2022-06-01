class Solution(object):
    def longestMountain(self, arr):
        N = len(arr)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and arr[end] < arr[end + 1]:
                while end + 1 < N and arr[end] < arr[end + 1]:
                    end += 1

                if end + 1 < N and arr[end] > arr[end + 1]:
                    while end + 1 < N and arr[end] > arr[end + 1]:
                        end += 1
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans
