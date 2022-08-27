class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                res = nums[left] + nums[right] + nums[i]
                if res == 0:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif res > 0:
                    right -= 1
                else:
                    left += 1
        return ans
