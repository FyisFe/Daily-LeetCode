class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm = {}
        for letter in s:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1

        for letter in t:
            if letter not in hm or hm[letter] == 0:
                return False
            hm[letter] -= 1

        return True
