class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def findNext(arr, num):
            idx = arr.index(num)
            for i in range(idx + 1, len(arr)):
                if arr[i] > num:
                    return arr[i]

            return -1

        return [findNext(nums2, num) for num in nums1]
