class Solution:
    def countVowelStrings(self, n: int) -> int:
        hm = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

        for i in range(1, n):
            prev = 0
            for key in hm:
                hm[key] += prev
                prev = hm[key]

        ans = 0
        for key in hm:
            ans += hm[key]

        return ans
