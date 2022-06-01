class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_arr = text.split(" ")
        res = 0
        for word in text_arr:
            res += 1
            for letter in word:
                if letter in brokenLetters:
                    res -= 1
                    break
        return res
