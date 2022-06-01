class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, cnt, n = nums[0], 1, len(nums)

        for i in range(1, n):
            if cur == nums[i]:
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                cur = nums[i]
                cnt -= 1

        return cur
