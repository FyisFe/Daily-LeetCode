class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + prefix_sum
            prefix_sum = nums[i]
        return nums
