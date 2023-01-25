class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(": ")", "[": "]", "{": "}"}

        for str in s:
            if str in map:
                stack.append(str)
            else:
                if not stack or map[stack.pop()] != str:
                    return False

        return not stack
