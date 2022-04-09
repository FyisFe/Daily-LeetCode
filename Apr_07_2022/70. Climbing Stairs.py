class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]

        for i in range(2, n + 1):
            arr.append(arr[i] + arr[i - 1])

        return arr[n]
