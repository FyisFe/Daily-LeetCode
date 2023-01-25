class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm, requiredHm = {}, {}

        def isSatisfied(curHm, reqHm):
            for key in reqHm:
                if key not in curHm or curHm[key] < reqHm[key]:
                    return False

            return True

        for str in t:
            if str in requiredHm:
                requiredHm[str] += 1
            else:
                requiredHm[str] = 1

        start = 0
        ansLen = float("inf")
        ansS, ansE = 0, 0

        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1

            while isSatisfied(hm, requiredHm):
                if i - start + 1 < ansLen:
                    ansS = start
                    ansE = i
                    ansLen = ansE - ansS + 1

                hm[s[start]] -= 1
                start += 1

        if ansLen == float("inf"):
            return ""
        return s[ansS : ansE + 1]
