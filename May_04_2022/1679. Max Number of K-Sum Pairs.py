class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hm = {}
        ans = 0
        for num in nums:
            if num in hm and hm[num] > 0:
                ans += 1
                hm[num] -= 1
            else:
                if k - num in hm:
                    hm[k - num] += 1
                else:
                    hm[k - num] = 1
        return ans
