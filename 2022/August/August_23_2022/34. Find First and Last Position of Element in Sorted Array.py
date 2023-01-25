class Solution:
    def searchRange(self, nums, target: int):
        left, right = 0, len(nums) - 1
        s, e = -1, -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left += 1
            elif nums[mid] == target:
                s = mid
                right = mid - 1
            else:
                right = mid - 1

        e = s
        while e + 1 < len(nums) and nums[e + 1] == target:
            e += 1
        return [s, e]
