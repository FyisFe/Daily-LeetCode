class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates = sorted(candidates)
        ans = []

        def helper(arr, tmp):
            if not len(arr):
                return

            if sum(tmp) + arr[0] == target:
                ans.append(tmp + [arr[0]])

            else:
                idx = 0
                len_arr = len(arr)
                while idx + 1 < len_arr and arr[idx + 1] == arr[idx]:
                    idx += 1
                idx += 1
                helper(arr[idx:], tmp)
                if sum(tmp) + arr[0] < target:
                    helper(arr[1:], tmp + [arr[0]])

        helper(candidates, [])
        return ans
