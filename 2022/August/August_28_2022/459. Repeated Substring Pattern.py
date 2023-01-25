class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getNext(pattern):
            n = len(pattern)
            next = [0 for _ in range(n)]
            prefixIdx = 0

            for i in range(1, n):
                while prefixIdx and pattern[prefixIdx] != pattern[i]:
                    prefixIdx = next[prefixIdx - 1]

                if pattern[i] == pattern[prefixIdx]:
                    prefixIdx += 1
                    next[i] = prefixIdx

            return next

        next = getNext(s)

        if next[-1] == 0:
            return False

        if len(s) % (len(s) - next[-1]) == 0:
            return True
        return False
