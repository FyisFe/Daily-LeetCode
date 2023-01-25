class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(cur, times, remain):
            if times == 0:
                return 1
            if times == 1:
                return cur * remain
            if times % 2:
                return helper(cur * cur, times // 2, cur * remain)
            else:
                return helper(cur * cur, times // 2, remain)

        ans = helper(x, abs(n), 1)
        return ans if n > 0 else 1 / ans
