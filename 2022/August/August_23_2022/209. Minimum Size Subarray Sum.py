class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        curSum = 0
        ans = float("inf")
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                ans = min(ans, i - start + 1)
                curSum -= nums[start]
                start += 1

        if ans == float("inf"):
            return 0
        else:
            return ans
