class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}

        for i in magazine:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for i in ransomNote:
            if i in hm and hm[i] > 0:
                hm[i] -= 1
            else:
                return False

        return True
