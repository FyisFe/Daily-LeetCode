class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans = 0
        arr = []
        for str in strs:
            arr.append([str.count("0"), str.count("1")])

        @cache
        def helper(zero, one, idx, size):
            nonlocal ans
            if zero <= m and one <= n:
                ans = max(ans, size)
            else:
                return

            if idx >= len(arr):
                return

            helper(zero, one, idx + 1, size)
            helper(arr[idx][0] + zero, arr[idx][1] + one, idx + 1, size + 1)

        helper(0, 0, 0, 0)

        return ans
