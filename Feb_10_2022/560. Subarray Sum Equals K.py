class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        sum = 0
        res = 0
        for num in nums:
            sum += num

            if sum - k in hm:
                res += hm[sum - k]

            if sum in hm:
                hm[sum] += 1
            else:
                hm[sum] = 1

        return res
