class Solution:
    def specialArray(self, nums) -> int:
        def count(x):
            cnt = 0
            for i in nums:
                if i >= x:
                    cnt += 1
            return cnt

        left = 0
        right = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            tmp = count(mid)

            if tmp == mid:
                return mid

            if tmp < mid:
                right = mid - 1

            else:
                left = mid + 1

        return -1
