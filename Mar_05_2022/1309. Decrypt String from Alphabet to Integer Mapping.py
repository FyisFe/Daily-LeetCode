class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0

        while i + 2 < len(s):
            if s[i + 2] == "#":
                res += chr(ord("a") + int(s[:2]) - 1)
                s = s[3:]
            else:
                res += chr(ord("a") + int(s[i]) - 1)
                s = s[1:]

        for cr in s:
            res += chr(ord("a") + int(cr) - 1)

        return res


sol = Solution()
print(sol.freqAlphabets("10#11#12"))
