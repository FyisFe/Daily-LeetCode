class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i, already_changed, N = 0, False, len(nums)
        while i < N - 1:
            if nums[i] <= nums[i + 1]:
                i += 1
                continue

            # if nums[i] > nums[i+1] then

            if already_changed:
                return False
            if i == 0 or (i and nums[i - 1] <= nums[i + 1]):
                already_changed = True
            else:
                already_changed = True
                nums[i + 1] = nums[i]
            i += 1
        return True
