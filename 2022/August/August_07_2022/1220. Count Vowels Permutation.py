class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

        for i in range(1, n):
            e = dp["a"] + dp["i"]
            a = dp["e"] + dp["i"] + dp["u"]
            i = dp["e"] + dp["o"]
            o = dp["i"]
            u = dp["o"] + dp["i"]

            dp["e"] = e
            dp["a"] = a
            dp["i"] = i
            dp["o"] = o
            dp["u"] = u

        return sum(dp.values()) % 1000000007
