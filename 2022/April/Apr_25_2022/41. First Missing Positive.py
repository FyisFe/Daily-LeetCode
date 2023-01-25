class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        idx = 0

        while idx < n:
            if nums[idx] == idx + 1:
                idx += 1
                continue

            if nums[idx] > 0 and nums[idx] <= n and nums[idx] != nums[nums[idx] - 1]:
                res = nums[idx]
                nums[idx] = nums[res - 1]
                nums[res - 1] = res
                continue

            idx += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
