class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))  # copy all and paste

        return dp[-1]
