class Solution:
    def search(self, nums, target: int) -> int:
        """
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

        sorted_nums = nums[pivot:] + nums[:pivot]
        left = 0
        right = len(sorted_nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] == target:
                return (mid + pivot) % len(sorted_nums)

            if sorted_nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:  # left part is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right part is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
