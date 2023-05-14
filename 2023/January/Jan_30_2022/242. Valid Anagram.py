class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for str in s:
            if str in hm:
                hm[str] += 1
            else:
                hm[str] = 1

        for str in t:
            if str not in hm:
                return False
            if hm[str] <= 0:
                return False
            hm[str] -= 1

        for key in hm:
            if hm[key] != 0:
                return False
        return True
