class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, len_p, len_s = {}, [], len(p), len(s)

        if len_p > len_s:
            return res

        for i in p:
            hm[i] = 1 if i not in hm else hm[i] + 1

        for i in range(len_p - 1):
            if s[i] in hm:
                hm[s[i]] -= 1

        for i in range(-1, len_s - len_p + 1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1

            if i + len_p < len_s and s[i + len_p] in hm:
                hm[s[i + len_p]] -= 1

            if all(v == 0 for v in hm.values()):
                res.append(i + 1)

        return res
