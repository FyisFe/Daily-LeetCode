class Solution:
    def countNegatives(self, grid) -> int:
        prev_col = len(grid[0]) - 1

        def bs(arr):
            left = 0
            nonlocal prev_col
            right = prev_col

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] >= 0:
                    left = mid + 1

                else:
                    right = mid - 1
            if right + 1 <= len(grid[0]) - 1:
                prev_col = right + 1
            return len(arr) - right - 1

        ans = 0
        for i in grid:
            ans += bs(i)

        return ans


sol = Solution()
sol.countNegatives([[3, 2], [1, 0]])
