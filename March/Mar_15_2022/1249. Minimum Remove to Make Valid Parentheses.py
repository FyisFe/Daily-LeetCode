class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        _s = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) != 0:
                    stack.pop()
                else:
                    _s[i] = ""

        for item in stack:
            _s[item] = ""
        return "".join(_s)
