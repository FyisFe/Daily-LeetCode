class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            elif len(stack):
                stack.pop(-1)
        s = "".join(stack)

        stack = []
        for i in t:
            if i != "#":
                stack.append(i)
            elif len(stack):
                stack.pop(-1)

        return s == "".join(stack)
