class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] = -1
            else:
                hm[s[i]] = i

        for k in s:
            if hm[k] != -1:
                return hm[k]

        return -1
