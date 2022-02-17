class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        end = len(candidates) - 1

        def helper(cur_idx, cur_num, arr):
            if cur_idx > end:
                return

            num = candidates[cur_idx]
            helper(cur_idx + 1, cur_num, arr)

            if num + cur_num == target:
                arr = arr + [num]
                ans.append(arr)
                return

            if num + cur_num < target:
                arr = arr + [num]
                helper(cur_idx, cur_num + num, arr)

        helper(0, 0, [])
        return ans
