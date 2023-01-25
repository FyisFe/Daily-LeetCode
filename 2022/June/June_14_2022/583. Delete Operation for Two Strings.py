class Solution:
    def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = [0] * (n + 1)
        for i in range(m):
            prev = 0
            for j in range(n):
                prev, dp[j + 1] = dp[j + 1], max(
                    dp[j], dp[j + 1], prev + (w1[i] == w2[j])
                )
        return m + n - 2 * dp[n]
