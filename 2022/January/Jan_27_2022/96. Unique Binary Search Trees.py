class Solution:
    def numTrees(self, n):
        """You can choose any value as the root of the tree. But for every value you choose, you basically divide everything else into two sub trees. Meaning, that for every root value, the total number of trees is just going to be the permutations of the right subtree multiplied by the permutations of the left subtree."""
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, len(dp)):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
