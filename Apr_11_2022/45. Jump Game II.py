class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])

        return dp[-1]
