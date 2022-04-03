class Solution:
    def twoSum(self, nums, target: int):
        hm = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hm:
                return [i, hm[nums[i]]]

            hm[diff] = i
