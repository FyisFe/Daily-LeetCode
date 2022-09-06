class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        cumulativeSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cumulativeSum[i] = cumulativeSum[i - 1] + nums[i - 1]

        remainderHm = {}
        for count in cumulativeSum:
            if count % k in remainderHm:
                remainderHm[count % k] += 1
            else:
                remainderHm[count % k] = 1
        ans = 0
        for key in remainderHm:
            ans += (remainderHm[key] * (remainderHm[key] - 1)) // 2
        return ans
