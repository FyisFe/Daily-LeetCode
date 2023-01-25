class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n

        dp = [float("inf") for _ in range(n + 1)]
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3

        for i in range(4, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - (j * j)])

        return dp[-1]
