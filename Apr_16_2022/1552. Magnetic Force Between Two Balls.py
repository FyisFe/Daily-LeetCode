class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        left = 1
        right = (position[-1] - position[0]) // (m - 1) + 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            cnt = 1
            cur = position[0]

            for p in position[1:]:
                if p - cur >= mid:
                    cnt += 1
                    cur = p
                    if cnt >= m:
                        break

            if cnt >= m:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1

        return ans
