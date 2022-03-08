class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        s = -1
        e = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    s = mid
                right = mid - 1
        e = s
        while e + 1 < len(nums) and nums[e + 1] == target:
            e += 1

        return [s, e]
