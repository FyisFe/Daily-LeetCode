class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [(i, i) for i in range(n)]

        def isPalindrome(st):
            return st == st[::-1]

        for i in range(1, n):
            start = max(dp[i - 1][0] - 1, 0)
            for j in range(start, i):
                if isPalindrome(s[j : i + 1]):
                    dp[i] = (j, i)
                    break

        res = max(dp, key=lambda x: x[1] - x[0])
        return s[res[0] : res[1] + 1]
