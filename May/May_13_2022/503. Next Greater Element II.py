class Solution:
    def nextGreaterElements(self, nums):
        hm = {}
        n = len(nums)
        nums = nums + nums
        stack = []
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop(-1)
            hm[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])

        return [hm[i] for i in range(n)]
