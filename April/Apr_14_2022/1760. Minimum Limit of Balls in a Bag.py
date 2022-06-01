class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = left + (right - left) // 2
            count = self.count(mid, nums)
            if count <= maxOperations:
                right = mid
            else:
                left = mid + 1
        return right  # or l

    def count(self, n, arr):
        return sum((a - 1) // n for a in arr)
