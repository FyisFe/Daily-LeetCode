class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for st in s:
            if st in hm:
                hm[st] += 1
            else:
                hm[st] = 1

        sorted_hm = sorted(hm.items(), key=operator.itemgetter(1), reverse=True)

        ans = [key * val for (key, val) in sorted_hm]

        return "".join(ans)
