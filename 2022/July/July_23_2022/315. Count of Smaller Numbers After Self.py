class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]

        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                L = nums[:mid]
                R = nums[mid:]
                mergeSort(L)
                mergeSort(R)

                # Merging Starts
                i, j, k = 0, 0, 0
                while i < len(L) and j < len(R):
                    if L[i][0] > R[j][0]:
                        ans[L[i][1]] += len(R) - j
                        nums[k] = L[i]
                        i += 1
                    else:
                        nums[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    nums[k] = L[i]
                    k += 1
                    i += 1
                while j < len(R):
                    nums[k] = R[j]
                    j += 1
                    k += 1

        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        mergeSort(nums)
        return ans
