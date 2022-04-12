class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r_s = ""
        for i in s:
            if i != "#":
                r_s += i
            else:
                r_s = r_s[:-1]

        r_t = ""
        for i in t:
            if i != "#":
                r_t += i
            else:
                r_t = r_t[:-1]

        return r_s == r_t
