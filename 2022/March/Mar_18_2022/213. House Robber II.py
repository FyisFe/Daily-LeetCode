class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]

            for i in range(1, len(nums)):
                dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
            return dp[-1]

        a = helper(nums[1:])
        b = helper(nums[:-1])
        return max(a, b)
