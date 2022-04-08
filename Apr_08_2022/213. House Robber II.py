class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            dp = arr
            dp[1] = max(dp[1], dp[0])

            for i in range(2, len(arr)):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(helper(nums[1:]), helper(nums[:-1]))
