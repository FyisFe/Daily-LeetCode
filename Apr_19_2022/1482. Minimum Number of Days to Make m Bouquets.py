class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        left = 1
        right = max(bloomDay)
        ans = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            idx = 0

            while idx < n:
                canBloom = True
                for i in range(k):
                    if idx + i >= n or bloomDay[idx + i] > mid:
                        canBloom = False
                        idx += i + 1
                        break
                if canBloom:
                    cnt += 1
                    idx += k

            if cnt < m:
                left = mid + 1
            else:
                ans = min(ans, mid)
                right = mid - 1
        return ans


sol = Solution()
sol.minDays([1, 10, 3, 10, 2], 3, 1)
