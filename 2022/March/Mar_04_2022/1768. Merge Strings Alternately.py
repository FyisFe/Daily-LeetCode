class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        flip = False
        while word1 and word2:
            if not flip:
                res += word1[0]
                word1 = word1[1:]
                flip = not flip
            else:
                res += word2[0]
                word2 = word2[1:]
                flip = not flip

        if word1:
            return res + word1
        else:
            return res + word2
