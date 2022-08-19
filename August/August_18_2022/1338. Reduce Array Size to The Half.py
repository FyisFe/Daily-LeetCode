class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hm = {}
        for i in arr:
            if i in hm:
                hm[i] += 1

            else:
                hm[i] = 1

        frequencyList = sorted(list(hm.values()), reverse=True)

        totalSizeRequired = len(arr) // 2
        curSize = 0
        ans = 0
        for freq in frequencyList:
            ans += 1
            curSize += freq
            if curSize >= totalSizeRequired:
                return ans
