class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for chr in s:
            if (ord(chr.lower()) >= ord("a") and ord(chr.lower()) <= ord("z")) or (
                ord(chr.lower()) >= ord("0") and ord(chr.lower()) <= ord("9")
            ):
                str += chr.lower()
        left = 0
        right = len(str) - 1

        while left <= right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
        return True
