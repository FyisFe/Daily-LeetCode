class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                continue

            if len(stack) == 0:
                return False

            elif i == ")":
                if not stack.pop(-1) == "(":
                    return False

            elif i == "}":
                if not stack.pop(-1) == "{":
                    return False

            elif not stack.pop(-1) == "[":
                return False

        return len(stack) == 0
