class Solution:
    def addToArrayForm(self, num, k: int):

        carry = 0
        idx = len(num) - 1
        while k > 0:
            if idx < 0:
                tmp = (k % 10) + carry
                num = [tmp % 10] + num
            else:
                tmp = num[idx] + (k % 10) + carry
                num[idx] = tmp % 10
            carry = tmp // 10
            idx -= 1
            k = k // 10

        while carry:
            if idx < 0:
                num = [carry] + num
                return num
            else:
                tmp = num[idx] + carry
                num[idx] = tmp % 10
                carry = tmp // 10
                idx -= 1

        return num
