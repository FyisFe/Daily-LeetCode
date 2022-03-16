class Solution:
    def permuteUnique(self, nums):
        nums = sorted(nums)
        ans = []

        def helper(arr, tmp):
            if len(arr) == 1:
                ans.append(tmp + arr)
            elif len(arr) == 2:
                ans.append(tmp + arr)
                if arr[0] != arr[1]:
                    ans.append(tmp + arr[::-1])
            else:
                idx = 0
                len_arr = len(arr)
                while idx < len_arr:
                    helper(arr[0:idx] + arr[idx + 1 :], tmp + [arr[idx]])
                    while idx + 1 < len_arr and arr[idx] == arr[idx + 1]:
                        idx += 1
                    idx += 1

        helper(nums, [])
        return ans
