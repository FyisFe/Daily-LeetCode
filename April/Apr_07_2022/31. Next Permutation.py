class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        pivot = -1
        while j > 0:
            if nums[j] > nums[j - 1]:
                pivot = j - 1
                break
            j -= 1

        if pivot == -1:
            nums = nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]
        i = pivot + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
