class Solution:
    def findSubsequences(self, A: List[int]) -> List[List[int]]:
        result, N = set(), len(A)

        def backtrack(cur, index):
            if index == N:
                return
            for i in range(index, N):
                c = A[i]
                if cur and c < cur[-1]:
                    continue

                cur.append(c)
                if len(cur) > 1:
                    result.add(tuple(cur))
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)
        return result
