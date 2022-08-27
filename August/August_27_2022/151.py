class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = " " + s + " "
        start = end = -1
        for i in range(len(s) - 2, 0, -1):
            if s[i + 1] == " " and s[i] != " ":
                end = i
            if s[i - 1] == " " and s[i] != " ":
                start = i
                res = res + " " + s[start : end + 1]
        return res[1:]
