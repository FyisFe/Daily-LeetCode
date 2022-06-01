class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums_left, cur, res):
            if not nums_left:
                res.append(cur)
                return

            for i in range(len(nums_left)):
                helper(nums_left[:i] + nums_left[i + 1 :], cur + [nums_left[i]], res)

        res = []
        helper(nums, [], res)
        return res
