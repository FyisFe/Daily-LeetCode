class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 10:
            return []
        ans = set()
        hm = {}

        for i in range(0, len(s) - 9):
            t = s[i : i + 10]
            if t in hm:
                ans.add(t)
            else:
                hm[s[i : i + 10]] = 1

        return list(ans)
