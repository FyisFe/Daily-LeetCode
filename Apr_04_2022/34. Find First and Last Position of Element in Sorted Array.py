class Solution:
    def searchRange(self, nums, target: int):
        # find left most one
        left = 0
        right = len(nums) - 1
        left_most = -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                left_most = mid
                right = mid - 1

            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        if left_most == -1:
            return [-1, -1]

        # find right most one
        left = left_most
        right = len(nums) - 1
        right_most = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                right_most = mid
                left = mid + 1

            if nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return [left_most, right_most]
