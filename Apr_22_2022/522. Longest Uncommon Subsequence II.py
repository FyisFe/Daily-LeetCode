class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(reverse=True, key=len)

        def _isSubsequence(s1: str, s2: str) -> bool:
            i = 0
            j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1

            return i == len(s1)

        for i in range(len(strs)):
            found = False
            for j in range(len(strs)):
                if i == j:
                    continue

                found = _isSubsequence(strs[i], strs[j])
                if found:
                    break

            if not found:
                return len(strs[i])

        return -1
