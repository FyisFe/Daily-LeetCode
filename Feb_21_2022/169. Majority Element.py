class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 1

        for num in nums[1:]:
            if cur == num:
                count += 1

            else:
                count -= 1

            if count == 0:
                cur = num
                count = 1

        return cur
