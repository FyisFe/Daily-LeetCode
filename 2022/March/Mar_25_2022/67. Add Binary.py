class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        a_len = len(a)
        b_len = len(b)
        i = a_len - 1
        j = b_len - 1
        res = ""
        carry = 0
        while j >= 0:
            tmp = int(a[i]) + int(b[j]) + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            j -= 1
            i -= 1

        while i >= 0:
            tmp = int(a[i]) + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i -= 1

        if carry:
            res = "1" + res

        return res
