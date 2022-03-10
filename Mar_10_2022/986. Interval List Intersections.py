class Solution:
    def intervalIntersection(self, firstList, secondList):
        f_len = len(firstList)
        s_len = len(secondList)

        f = 0
        s = 0

        res = []

        while f < f_len and s < s_len:
            f_s, f_e = firstList[f][0], firstList[f][1]
            s_s, s_e = secondList[s][0], secondList[s][1]

            if f_e < s_s:
                f += 1
                continue

            if s_e < f_s:
                s += 1
                continue

            res.append([max(f_s, s_s), min(f_e, s_e)])

            if f_e == s_e:
                f += 1
                s += 1
            elif f_e < s_e:
                f += 1
            else:
                s += 1

        return res
