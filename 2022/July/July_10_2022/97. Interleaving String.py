class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def rec(index1, index2, index3):

            if index1 == len(s1):
                return s2[index2:] == s3[index3:]

            if index2 == len(s2):
                return s1[index1:] == s3[index3:]

            ans = False
            if s1[index1] == s3[index3]:
                ans = rec(index1 + 1, index2, index3 + 1)

            if ans:
                return ans

            if ans == False and s2[index2] == s3[index3]:
                ans = rec(index1, index2 + 1, index3 + 1)

            return ans

        return rec(0, 0, 0)
