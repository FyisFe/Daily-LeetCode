class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) == 1:
            return [x for x in dict[digits[0]]]

        digits = digits[::-1]

        ans = [x for x in dict[digits[0]]]

        for digit in digits[1:]:
            next = []
            for chr in dict[digit]:
                for tmp in ans:
                    next.append(chr + tmp)
            ans = next

        return ans
