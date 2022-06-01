class Solution:
    def construct2DArray(self, original, m: int, n: int):
        if len(original) != m * n:
            return []

        idx = 0
        ans = []
        col_arr = []
        while idx < len(original):
            col_arr.append(original[idx])
            idx += 1

            if len(col_arr) == n:
                ans.append(col_arr)
                col_arr = []

        return ans
