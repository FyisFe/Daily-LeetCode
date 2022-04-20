class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        dp = [[1, 1]] * l
        max_length = 0

        for i in range(0, l):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            # print(dp[i])
            if dp[i][0] > max_length:
                max_length = dp[i][0]
                count = dp[i][1]
            elif dp[i][0] == max_length:
                count += dp[i][1]
        return count
