class Solution:
    def reinitializePermutation(self, n: int) -> int:
        ans = 0

        def isTheSame(arr):
            for i in range(len(arr)):
                if i != arr[i]:
                    return False
            return True

        perm = [i for i in range(n)]
        while True:
            arr = []
            for i in range(n):
                if i % 2 == 0:
                    arr.append(perm[i // 2])
                else:
                    arr.append(perm[n // 2 + (i - 1) // 2])
            ans += 1
            if isTheSame(arr):
                return ans
            perm = arr

        """
        If i % 2 == 0, then arr[i] = perm[i / 2].
        If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].

        Input: n = 4
        Output: 2
        Explanation: perm = [0,1,2,3] initially.
        After the 1st operation, perm = [0,2,1,3]
        After the 2nd operation, perm = [0,1,2,3]
        So it takes only 2 operations.
        """
