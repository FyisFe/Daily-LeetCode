class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        sum, left = 0, 0
        n_l = len(nums)

        for right in range(0, n_l):
            sum += nums[right]
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1

        if ans == float("inf"):
            return 0
        return ans
