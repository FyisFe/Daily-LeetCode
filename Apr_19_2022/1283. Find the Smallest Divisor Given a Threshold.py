class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            cur_sum = 0
            for num in nums:
                if num <= mid:
                    cur_sum += 1
                else:
                    cur_sum += math.ceil(num / mid)

            if cur_sum > threshold:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1

        return ans
