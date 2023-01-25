class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = res = sum(i * num for i, num in enumerate(nums))
        n, s = len(nums), sum(nums)

        for i in range(n - 1, 0, -1):
            f += s - n * nums[i]
            res = max(res, f)

        return res
