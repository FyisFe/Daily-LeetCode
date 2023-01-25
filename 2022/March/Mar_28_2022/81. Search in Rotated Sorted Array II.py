class Solution:
    def search(self, nums, target: int) -> bool:
        pivot = 0
        found = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                pivot += 1
            else:
                pivot = i + 1
                found = True
                break

        if found:
            sorted_nums = nums[pivot:] + nums[:pivot]
        else:
            sorted_nums = nums

        left = 0
        right = len(sorted_nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] == target:
                return True

            if sorted_nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
