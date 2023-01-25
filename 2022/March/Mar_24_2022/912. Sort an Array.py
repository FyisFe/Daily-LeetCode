import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qsort(arr):
            if len(arr) <= 1:
                return arr
            idx = random.randint(0, len(arr) - 1)
            pivot = arr[idx]

            left = [i for i in arr[0:idx] + arr[idx + 1 : len(arr)] if i < pivot]
            right = [i for i in arr[0:idx] + arr[idx + 1 : len(arr)] if i >= pivot]

            return qsort(left) + [pivot] + qsort(right)

        return qsort(nums)
