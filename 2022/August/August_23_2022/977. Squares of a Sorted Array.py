class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        find the first non-negative num
        """

        left, right = 0, len(nums) - 1
        target = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                target = mid
                right = mid - 1

        if target == 0:
            return [x ** 2 for x in nums]
        if target == -1:
            return [x ** 2 for x in reversed(nums)]

        negativeIdx = target - 1
        positiveIdx = target
        ans = []
        while negativeIdx >= 0 and positiveIdx < len(nums):
            if abs(nums[negativeIdx]) > abs(nums[positiveIdx]):
                ans.append(nums[positiveIdx] ** 2)
                positiveIdx += 1
            else:
                ans.append(nums[negativeIdx] ** 2)
                negativeIdx -= 1

        while negativeIdx >= 0:
            ans.append(nums[negativeIdx] ** 2)
            negativeIdx -= 1

        while positiveIdx < len(nums):
            ans.append(nums[positiveIdx] ** 2)
            positiveIdx += 1

        return ans
