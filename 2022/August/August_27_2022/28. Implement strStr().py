class KMP:
    def __init__(self, text, pattern) -> None:
        self.text, self.pattern = text, pattern

    def getNext(self):
        n = len(self.pattern)
        next = [0 for _ in range(n)]
        prefixIdx = 0

        for i in range(1, n):
            while prefixIdx and self.pattern[prefixIdx] != self.pattern[i]:
                prefixIdx = next[prefixIdx - 1]

            if self.pattern[i] == self.pattern[prefixIdx]:
                prefixIdx += 1
                next[i] = prefixIdx

        return next

    def match(self):
        n = len(self.pattern)
        next = self.getNext()
        i = 0
        for idx, chr in enumerate(self.text):
            while i and self.pattern[i] != chr:
                i = next[i - 1]

            if self.pattern[i] == chr:
                if i == n - 1:
                    return idx - i
                else:
                    i += 1
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return KMP(haystack, needle).match()
