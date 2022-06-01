class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hm_s = {}
        hm_e = {}
        min_s = float("inf")
        max_e = -float("inf")
        for c, s, e in trips:
            if s < min_s:
                min_s = s
            if s in hm_s:
                hm_s[s] += c
            else:
                hm_s[s] = c

            if e > max_e:
                max_e = e
            if e in hm_e:
                hm_e[e] += c
            else:
                hm_e[e] = c

        cur = capacity
        for i in range(min_s, max_e + 1):
            c = 0
            if i in hm_s:
                c += hm_s[i]
            if i in hm_e:
                c -= hm_e[i]
            if c > cur:
                return False

            cur -= c

        return True
