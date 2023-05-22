# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         redCnt, whiteCnt, blueCnt = 0, 0, 0
#         for num in nums:
#             if num == 0:
#                 redCnt += 1
#             elif num == 1:
#                 whiteCnt += 1
#             else:
#                 blueCnt += 1


#         for i in range(redCnt):
#             nums[i] = 0
#         for i in range(whiteCnt):
#             nums[redCnt + i] = 1
#         for i in range(blueCnt):
#             nums[redCnt + whiteCnt + i] = 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
