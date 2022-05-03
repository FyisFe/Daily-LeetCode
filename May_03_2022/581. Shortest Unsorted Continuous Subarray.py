class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        s = 0
        found = False
        e = len(nums) - 1

        while s < e:
            if nums[s] != sorted_nums[s]:
                found = True
                break
            s += 1

        if not found:
            return 0

        while e > s:
            if nums[e] != sorted_nums[e]:
                return e - s + 1

            e -= 1
