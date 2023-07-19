class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
                cnt = 0
            else:
                if cnt == 0:
                    idx += 1
                    nums[idx] = nums[i]
                    cnt += 1

        return idx + 1
