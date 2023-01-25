class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        hm = {}
        count = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur:
                count += 1
            else:
                count -= 1

            if count is 0:
                res = i + 1

            if count in hm:
                res = max(res, i - hm[count])
            else:
                hm[count] = i

        return res
