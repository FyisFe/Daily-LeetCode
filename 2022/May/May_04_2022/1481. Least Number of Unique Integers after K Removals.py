class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        hm = {}
        for num in arr:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        hm = dict(sorted(hm.items(), key=lambda item: item[1]))
        ans = 0
        for key in hm:
            if hm[key] <= k:
                k -= hm[key]
                ans += 1
            else:
                return len(hm) - ans

        return len(hm) - ans
