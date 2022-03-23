class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        diff = 0

        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i - 1]

            if diff < 0 and cur_diff > 0:
                return False

            if diff > 0 and cur_diff < 0:
                return False

            diff += cur_diff

        return True
