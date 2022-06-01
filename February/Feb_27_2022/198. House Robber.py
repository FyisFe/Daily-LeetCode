class Solution:
    def rob(self, nums: List[int]) -> int:
        leng = len(nums)
        dp = [0] * (leng + 3)
        for i in range(leng - 1, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]
        return max(dp[0], dp[1])
