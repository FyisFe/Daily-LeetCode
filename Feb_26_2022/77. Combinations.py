class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(arr, path, res):
            if len(path) == k:
                res.append(path)
                return

            if not len(arr):
                return

            dfs(arr[1:], path + [arr[0]], res)
            dfs(arr[1:], path, res)

        arr = [i for i in range(1, n + 1)]
        res = []
        dfs(arr, [], res)
        return res
