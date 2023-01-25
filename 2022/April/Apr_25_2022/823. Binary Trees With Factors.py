MOD = 1000000007


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # smaller numbers multiply to form a larger number
        # after sorting we only have to worry about numbers
        # to the left of the current number
        arr.sort()
        # let dp[x] be the number of possible binary trees we
        # can form using x as the root
        dp = {x: 1 for x in arr}
        # iterate through each number, using it as the root
        for i in range(len(arr)):
            # iterate through all numbers smaller than the current
            # number
            for j in range(i):
                # check if big/small is in array, if yes, there'd be
                # dp[small]*dp[big/small] possible trees with big as
                # root
                if arr[i] / arr[j] in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i] / arr[j]]

        return sum(dp[x] for x in dp) % MOD
