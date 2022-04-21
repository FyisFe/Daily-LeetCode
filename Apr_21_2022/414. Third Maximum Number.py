class Solution:
    def thirdMax(self, nums) -> int:
        nums_set = set(nums)

        nums = sorted(list(nums_set), reverse=True)

        if len(nums) >= 3:
            return nums[2]

        return nums[-1]


sol = Solution()
sol.thirdMax([1, 2])
