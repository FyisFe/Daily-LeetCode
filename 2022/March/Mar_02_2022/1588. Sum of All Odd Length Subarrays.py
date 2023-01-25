class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_len = len(arr)
        res_len = 1
        res = 0
        while res_len <= arr_len:
            s = 0
            while s + res_len <= arr_len:
                for i in range(res_len):
                    res += arr[s + i]
                s += 1
            res_len += 2
        return res
