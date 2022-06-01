class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        current_diff = -1
        count = 0
        res = 0
        for i in range(1, len(nums)):
            new_diff = nums[i] - nums[i - 1]

            if new_diff != current_diff:
                current_diff = new_diff
                count = 1
            else:
                res += count
                count += 1

        return res
