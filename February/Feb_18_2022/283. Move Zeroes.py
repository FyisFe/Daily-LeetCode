class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)

        for i in range(arr_len):
            if nums[i] is 0:
                nums.remove(nums[i])
                nums.append(0)
                arr_len -= 1
