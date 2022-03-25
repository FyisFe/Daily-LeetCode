class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1

        while idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits
