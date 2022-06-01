class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return dict[s[0]]

        result = 0
        index = 0

        while index < len(s) - 1:
            if dict[s[index]] >= dict[s[index + 1]]:
                result += dict[s[index]]
            else:
                result -= dict[s[index]]

            index += 1

        return result + dict[s[-1]]
