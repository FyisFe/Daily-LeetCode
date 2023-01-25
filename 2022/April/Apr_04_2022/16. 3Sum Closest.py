class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        min_diff = float("inf")

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                sum = nums[left] + nums[right] + nums[i]

                if abs(sum - target) < min_diff:
                    min_diff = abs(sum - target)

                if sum > target:
                    right -= 1
                else:
                    left += 1

            if min_diff == 0:
                return target

        return target - min_diff


sol = Solution()
sol.threeSumClosest([-1, 2, 1, -4], 1)
