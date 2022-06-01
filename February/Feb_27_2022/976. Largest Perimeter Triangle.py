class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(2, n):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if b + c > a:
                return a + b + c
        return 0
