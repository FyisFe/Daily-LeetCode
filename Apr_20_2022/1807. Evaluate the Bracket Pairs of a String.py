class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        hm = {}

        for words in knowledge:
            hm[words[0]] = words[1]

        i = 0
        ans = ""
        while i < len(s):
            if s[i] != "(":
                ans += s[i]
                i += 1

            else:
                word = ""
                j = i + 1
                while s[j] != ")":
                    word += s[j]
                    j += 1
                i = j + 1
                if word in hm:
                    ans += hm[word]
                else:
                    ans += "?"

        return ans
