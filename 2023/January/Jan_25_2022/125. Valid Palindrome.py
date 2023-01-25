class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        convertedS = ""
        for str in s:
            if str.isalnum():
                convertedS += str

        s, e = 0, len(convertedS) - 1

        while s < e:
            if convertedS[s] != convertedS[e]:
                return False

            s += 1
            e -= 1

        return True
