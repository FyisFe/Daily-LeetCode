class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        n = len(nums)
        summ = 0
        ans = 0
        for i in range(n):
            summ += nums[i]
            ans += d[summ % k]
            d[summ % k] += 1
        return ans
