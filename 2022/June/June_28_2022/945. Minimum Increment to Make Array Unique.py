class Solution:
    def minIncrementForUnique(self, nums) -> int:
        nums = sorted(nums)
        min_possible = nums[0] + 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < min_possible:
                ans += min_possible - nums[i]
                nums[i] = min_possible
            min_possible = nums[i] + 1

        return ans
