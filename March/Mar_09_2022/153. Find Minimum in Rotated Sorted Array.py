class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left] and nums[mid] <= nums[right]:
                pivot = left
                break
            if nums[mid] < nums[left]:
                right = mid

            elif nums[mid] > nums[right]:
                left = mid + 1

        return nums[pivot]
