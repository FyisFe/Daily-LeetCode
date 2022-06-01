class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ord_arr = [0 for _ in range(n)]
        k = k - n
        idx = 0
        while k > 25:
            ord_arr[idx] += 25
            k -= 25
            idx += 1
        ord_arr[idx] = k

        res = ""
        ord_arr = reversed(ord_arr)

        for i in ord_arr:
            res += chr(i)

        return res
