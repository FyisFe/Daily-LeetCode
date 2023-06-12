class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

        ans = 0
        hasOdd = False

        for i in hm:
            if hm[i] % 2 == 0:
                ans += hm[i]
            else:
                ans += hm[i] - 1
                hasOdd = True

        if hasOdd:
            ans += 1

        return ans
