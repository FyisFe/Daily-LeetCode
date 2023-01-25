class Solution:
    def minimumDeletions(self, nums) -> int:
        n = len(nums)

        min_num = min(nums)
        max_num = max(nums)

        min_num_idx = nums.index(min_num)
        max_num_idx = nums.index(max_num)

        return min(
            max(min_num_idx, max_num_idx) + 1,
            n - min(min_num_idx, max_num_idx),
            n - (max(min_num_idx, max_num_idx) - min(min_num_idx, max_num_idx)) + 1,
        )
