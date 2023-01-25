class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        hm = {}
        for word in words:
            str = ""
            for char in word:
                str += lst[ord(char) - 97]
            if str not in hm:
                hm[str] = 1
        return len(hm)
