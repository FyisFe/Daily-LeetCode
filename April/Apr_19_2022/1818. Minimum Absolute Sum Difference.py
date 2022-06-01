class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        len1 = len(nums1)
        max_diff = sum_abs_diff = 0
        for a, b in zip(nums1, nums2):
            abs_diff = abs(a - b)
            sum_abs_diff += abs_diff
            idx = bisect_left(nums1, b)
            if idx < len1:
                max_diff = max(max_diff, abs_diff - abs(nums1[idx] - b))
            if idx > 0:
                max_diff = max(max_diff, abs_diff - abs(nums1[idx - 1] - b))
        return (sum_abs_diff - max_diff) % 1_000_000_007
