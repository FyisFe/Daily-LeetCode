class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1

            if t[i] in dict:
                dict[t[i]] -= 1
            else:
                dict[t[i]] = -1

        if t[-1] in dict:
            dict[t[-1]] -= 1
        else:
            dict[t[-1]] = -1

        for t in dict:
            if dict[t]:
                return t
