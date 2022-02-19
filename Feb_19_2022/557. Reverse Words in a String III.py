class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(" "))

        for i in range(len(l)):
            l[i] = l[i][::-1]

        return " ".join(l)
