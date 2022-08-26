class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for letter in magazine:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1

        for letter in ransomNote:
            if letter not in hm:
                return False
            if hm[letter] <= 0:
                return False
            hm[letter] -= 1

        return True
