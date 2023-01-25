class Solution:
    def wordCount(self, s: List[str], t: List[str]) -> int:

        hm = {}
        for i in s:
            x = "".join(sorted(i))
            hm[x] = 1

        ans = 0
        for i in t:
            i = "".join(sorted(i))
            for j in range(len(i)):
                x = i[:j] + i[j + 1 :]
                if x in hm:
                    ans += 1
                    break
        return ans
