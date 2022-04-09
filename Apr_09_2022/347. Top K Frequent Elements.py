class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        dict = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        ans = []
        cnt = 0

        for (num, val) in dict:
            if cnt == k:
                break
            ans.append(num)
            cnt += 1

        return ans
