import operator


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        sorted_hm = sorted(hm.items(), key=operator.itemgetter(1), reverse=True)

        ans = [key for (key, val) in sorted_hm]

        return ans
