class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # monotonic stack
        stack = []

        n = len(nums)

        for i, num in enumerate(nums):
            while stack and num < stack[-1] and (len(stack) + n - i) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)

        return stack

    # TLE
    # def mostCompetitive(self, nums, k: int):
    #     n = len(nums)
    #     ans = []
    #     i = 0
    #     prev = 0
    #     while len(ans) < k:
    #         min_num = min(nums)
    #         idx = nums.index(min_num)
    #         # 3 5 2 6
    #         # 2
    #         tmp = []
    #         while prev + idx > n - k + i:
    #             tmp.append((idx, nums[idx]))
    #             nums[idx] = float("inf")
    #             min_num = min(nums)
    #             idx = nums.index(min_num)
    #         for pos, val in tmp:
    #             nums[pos] = val
    #         ans.append(nums[idx])
    #         prev = prev + idx + 1
    #         nums = nums[idx + 1 :]
    #         i += 1

    #     return ans
