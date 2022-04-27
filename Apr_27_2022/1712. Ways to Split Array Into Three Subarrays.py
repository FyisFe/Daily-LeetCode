class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        pre_sum = [0]
        for n in nums:
            pre_sum.append(pre_sum[-1] + n)
        length = len(nums)
        ret, mid_l, mid_r = 0, 0, 0
        for i in range(1, length):
            mid_l = max(mid_l, i + 1)
            while mid_l < length and 2 * pre_sum[i] > pre_sum[mid_l]:
                mid_l += 1
            mid_r = max(mid_r, mid_l)
            while mid_r < length and 2 * pre_sum[mid_r] <= pre_sum[i] + pre_sum[-1]:
                mid_r += 1
            ret += mid_r - mid_l
        return ret % 1_000_000_007
