class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        def subarray_sum(left, right):
            return prefix_sum[right + 1] - prefix_sum[left]

        nums.append(0)
        mono_stack = [-1]

        res = 0
        for i in range(n + 1):
            while nums[i] < nums[mono_stack[-1]]:
                next_larger = mono_stack.pop()
                res = max(
                    res, nums[next_larger] * subarray_sum(mono_stack[-1] + 1, i - 1)
                )
            mono_stack.append(i)
        return res % (10**9 + 7)
