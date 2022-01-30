class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if nums[0] == target:
            return 0

        if l < 2 and nums[0] != target:
            return -1

        if target < nums[0]:
            for i in reversed(range(l)):
                if nums[i] == target:
                    return i
                if nums[i] < nums[i - 1]:
                    return -1

        if target > nums[0]:
            for i in range(l):
                if nums[i] == target:
                    return i
                if i + 1 < l:
                    if nums[i] > nums[i + 1]:
                        return -1
            return -1
