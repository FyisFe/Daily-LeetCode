class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0

        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        keys = list(hm.keys())

        for i in range(len(keys) - 1, -1, -1):
            ans += i * hm[keys[i]]

        return ans
