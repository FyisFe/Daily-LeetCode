class Solution:
    def climbStairs(self, n: int) -> int:
        if n is 1:
            return 1
        arr = [0 for _ in range(n)]
        arr[0] = 1
        arr[1] = 2

        for i in range(2, n):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[n - 1]
